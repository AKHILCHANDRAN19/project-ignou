import os
import shutil
import textwrap
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Arrow, FancyArrowPatch
# Requires: pip install matplotlib-venn
from matplotlib_venn import venn2, venn2_circles
# Requires: pip install reportlab
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib import colors

# --- SCRIPT CONFIGURATION ---

# IMPORTANT: Set the output directory for your device.
# For Android Termux or Pydroid:
OUTPUT_DIR = '/storage/emulated/0/Download/'
# For Windows/Mac/Linux Desktops (uncomment the line below and comment the one above):
# OUTPUT_DIR = os.path.join(os.path.expanduser('~'), 'Downloads')

PDF_FILENAME = 'MMPH-009_Diagram_Solutions_Complete.pdf'
IMG_DIR = 'temp_diagram_images'

# --- DATA STRUCTURE: EXAM QUESTIONS AND SOLUTIONS ---

# Data from all 3 PDFs is included here.
EXAM_DATA = [
    # ==================== JUNE 2023 ====================
    {
        'year': 'June 2023',
        'question_number': 1,
        'question_text': "1. Briefly differentiate between Domestic vs. International Human Resource Management (IHRM). Discuss and describe various approaches to International Human Resource Management and their advantages and disadvantages.",
        'diagram_suggestion': "Diagram Suggestion: A table clearly differentiating DHRM and IHRM across key parameters (scope, risk, activities, etc.). For EPRG, a 2x2 matrix or a series of diagrams showing HQ-subsidiary staffing patterns for each approach."
    },
    {
        'year': 'June 2023',
        'question_number': 2,
        'question_text': "2. What do you understand by Strategic International Human Resource Management? What kinds of strategies are used by MNCs to compete in global markets? Discuss with relevant examples.",
        'diagram_suggestion': "Diagram Suggestion: A 2x2 matrix with 'Pressure for Global Integration' on one axis and 'Pressure for Local Responsiveness' on the other. The four quadrants would represent Global, Multidomestic, Transnational, and (perhaps) International (low on both, though less common as a distinct competitive strategy, often an early phase) strategies. Regional could be shown as a mid-point adaptation."
    },
    {
        'year': 'June 2023',
        'question_number': 3,
        'question_text': "3. “Training in preparing and supporting personnel on international assignments is an important process.” Describe and discuss.",
        'diagram_suggestion': "Diagram Suggestion: A timeline or flowchart showing the stages of an international assignment (Pre-Departure, In-Country, Pre-Repatriation) with the types of training and support relevant to each stage listed below."
    },
    {
        'year': 'June 2023',
        'question_number': 4,
        'question_text': "4. Briefly describe and discuss total reward system from the perspective of International Human Resource Management. What kinds of challenges are encountered by an expatriate in relation to taxation?",
        'diagram_suggestion': "Diagram Suggestion: A circular diagram of 'Total Rewards' with segments for Financial (Base Salary, Incentives, Allowances) and Non-Financial (Career Dev, Recognition, Work-Life Balance). For Taxation Challenges, a world map with arrows between two countries highlighting 'Double Tax Liability' and complex 'Tax Treaties'."
    },
    {
        'year': 'June 2023',
        'question_number': 5,
        'question_text': "5. Discuss and describe the theories of motivation and their perspective from international context.",
        'diagram_suggestion': "Diagram Suggestion: A table comparing the key tenets of each motivation theory and then a column discussing its 'Cross-Cultural Applicability/Considerations.' Highlight how cultural dimensions (e.g., individualism, power distance) might moderate the effects of each theory."
    },
    {
        'year': 'June 2023',
        'question_number': 6,
        'question_text': "6. Describe the principles and characteristics of high performance work systems and discuss how high performance organization is related to high performance work system.",
        'diagram_suggestion': "Diagram Suggestion: A diagram showing 'HPWS' (listing its characteristics/principles as inputs/components) leading to an arrow pointing to 'High Performance Organization' (listing its outcomes like superior results, adaptability, innovation)."
    },
    {
        'year': 'June 2023',
        'question_number': 7,
        'question_text': "7. Describe and discuss the role of employer's associations from international context.",
        'diagram_suggestion': "Diagram Suggestion: A diagram showing a central 'MNC' interacting with its 'Host Country Environment.' An 'Employer Association' (national level) influences the host country IR. Above this, an 'International Employer Association' (e.g., IOE, BusinessEurope) is shown influencing 'Supranational Bodies' (e.g., EU, ILO, OECD) which in turn influence the MNC's operating environment."
    },
    {
        'year': 'June 2023',
        'question_number': 8,
        'question_text': "8. Identify the trends and challenges faced by International Human Resource Managers. How can they be managed?",
        'diagram_suggestion': "Diagram Suggestion: A mind map with 'IHRM' at the center. One set of branches for 'Key Trends' (Globalization, Technology, Diversity, etc.) and another set for 'Key Challenges' (Talent, Culture, Compliance, etc.). Arrows could show how trends lead to challenges. A third set of branches could show 'Management Strategies'."
    },
    # ==================== JUNE 2024 ====================
    {
        'year': 'June 2024',
        'question_number': 1,
        'question_text': "1. Define and discuss the characteristics of International Human Resource Management. What are the similarities and differences between domestic and international human resource management?",
        'diagram_suggestion': "Diagram Suggestion: A Venn diagram showing DHRM as one circle and IHRM as a larger, encompassing circle. The overlapping section represents 'Core HR Functions.' The unique part of the IHRM circle lists 'Additional IHRM Activities & Complexities' (e.g., Expatriate Management, Cross-Cultural Issues, International Taxation)."
    },
    {
        'year': 'June 2024',
        'question_number': 2,
        'question_text': "2. What are the significant culture differences between individualistic society and collectivist society? Discuss the significant cultural difference between India and Turkey.",
        'diagram_suggestion': "Diagram Suggestion: A two-column table contrasting 'Individualistic Society' and 'Collectivist Society' across key aspects (Self-Concept, Goals, Relationships, etc.). For India vs. Turkey, another two-column table highlighting similarities (e.g., Collectivism, High Power Distance) and then specific distinguishing features for each."
    },
    {
        'year': 'June 2024',
        'question_number': 3,
        'question_text': "3. Who is an expatriate? What are the qualities required to become a successful expatriate? What are the main reasons for expatriate failure?",
        'diagram_suggestion': "Diagram Suggestion: A profile of a 'Successful Expatriate' highlighting key qualities in a star or circular diagram. For 'Expatriate Failure Reasons,' a fishbone (Ishikawa) diagram with the main bone 'Expat Failure' and branches for categories like 'Individual Factors,' 'Family Factors,' 'Organizational Factors,' and 'Host Country Factors.'"
    },
    {
        'year': 'June 2024',
        'question_number': 4,
        'question_text': "4. Explain the model of expatriate performance management. Why is it important to include hard, soft and contextual goals when assessing managerial performance?",
        'diagram_suggestion': "Diagram Suggestion: A visual representation of the expatriate performance management model from Unit 7... For the goals, a triangle with 'Hard,' 'Soft,' and 'Contextual' goals at its vertices, with 'Overall Managerial Performance' at the center."
    },
    {
        'year': 'June 2024',
        'question_number': 5,
        'question_text': "5. Discuss the relationship differences in leadership and motivation across cultures to the need for careful selection of expatriate managers. Compare and contrast leadership in France with leadership in the Arab World.",
        'diagram_suggestion': "Diagram Suggestion: A world map with call-out boxes for different regions ... Or, a two-circle Venn diagram comparing 'Leadership in France' and 'Leadership in Arab World,' showing both commonalities (e.g., hierarchical aspects) and differences."
    },
    # ==================== DECEMBER 2023 ====================
    {
        'year': 'December 2023',
        'question_number': 1,
        'question_text': "1. Describe and discuss any two cultural models and divergence and convergence of cultures.",
        'diagram_suggestion': "Diagram Suggestion: For Hofstede, the 'Cultural Onion Model' (Values, Rituals, Heroes, Symbols). For Trompenaars, a spider-web diagram showing the seven dimensions. For Convergence/Divergence, two initially separate circles representing cultures, with arrows of 'Globalization' either pushing them to overlap (Convergence) or showing them maintaining distinct spaces despite interaction (Divergence/Crossvergence)."
    },
    {
        'year': 'December 2023',
        'question_number': 2,
        'question_text': "2. Who is an expatriate? Discuss the reasons for the failures of an expatriate and how to overcome them, with examples.",
        'diagram_suggestion': "Diagram Suggestion: A cause-and-effect (fishbone) diagram showing 'Expatriate Failure' as the main effect, with branches for causes like 'Poor Selection,' 'Family Issues,' 'Cultural Inadaptability,' 'Lack of Training,' 'Insufficient Support.' For overcoming, a circular flow diagram showing 'Selection -> Training -> In-Country Support -> Repatriation Planning -> Successful Expat Cycle.'"
    },
    {
        'year': 'December 2023',
        'question_number': 3,
        'question_text': "3. How can one assess the performance of International employees and what criteria could be adopted for their performance?",
        'diagram_suggestion': "Diagram Suggestion: A model of IPM (similar to Unit 7) showing inputs (MNC Strategy, Assignment Task, Expat Characteristics) influencing the Expatriate Performance, which is then assessed using a 'Balanced Scorecard' type of approach with quadrants for Hard, Soft, Contextual, and Developmental criteria."
    },
]

# --- HELPER & DRAWING FUNCTIONS ---

def setup_directories():
    """Creates the output and temporary image directories."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    if os.path.exists(IMG_DIR):
        shutil.rmtree(IMG_DIR)
    os.makedirs(IMG_DIR)

def cleanup_directories():
    """Removes the temporary image directory."""
    if os.path.exists(IMG_DIR):
        shutil.rmtree(IMG_DIR)

def create_table_image(data, col_widths, title, filepath):
    """Creates an image of a table using Matplotlib."""
    # Count rows for figure height
    num_rows = len(data)
    fig_height = num_rows * 0.5 + 1 # Adjust multiplier as needed
    fig, ax = plt.subplots(figsize=(10, fig_height))
    ax.axis('tight')
    ax.axis('off')
    
    table_data_wrapped = []
    for row in data:
        wrapped_row = [textwrap.fill(str(cell), 35) for cell in row]
        table_data_wrapped.append(wrapped_row)

    table = ax.table(cellText=table_data_wrapped[1:], colLabels=table_data_wrapped[0],
                     loc='center', cellLoc='left', colWidths=col_widths)
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.8)

    # Style the header
    for (i, j), cell in table.get_celld().items():
        if i == 0:
            cell.set_text_props(weight='bold', color='white')
            cell.set_facecolor('#40466e')
        cell.get_text().set_multialignment('left')
        cell.set_edgecolor('w')

    plt.title(title, weight='bold', pad=20, fontsize=14)
    plt.savefig(filepath, bbox_inches='tight', dpi=150)
    plt.close()

def draw_2x2_matrix(title, xlabel, ylabel, q1, q2, q3, q4, midpoint, filepath):
    """Draws a 2x2 matrix diagram."""
    fig, ax = plt.subplots(figsize=(8, 7))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

    # Quadrants
    ax.text(2.5, 7.5, q1, ha='center', va='center', weight='bold', bbox=dict(facecolor='lightblue', alpha=0.5, boxstyle='round,pad=0.5'))
    ax.text(7.5, 7.5, q2, ha='center', va='center', weight='bold', bbox=dict(facecolor='lightgreen', alpha=0.5, boxstyle='round,pad=0.5'))
    ax.text(2.5, 2.5, q3, ha='center', va='center', weight='bold', bbox=dict(facecolor='lightcoral', alpha=0.5, boxstyle='round,pad=0.5'))
    ax.text(7.5, 2.5, q4, ha='center', va='center', weight='bold', bbox=dict(facecolor='lightgoldenrodyellow', alpha=0.5, boxstyle='round,pad=0.5'))

    if midpoint:
        ax.text(5, 5, midpoint, ha='center', va='center', style='italic', bbox=dict(facecolor='grey', alpha=0.3, boxstyle='round,pad=0.3'))

    # Axes and labels
    ax.axhline(5, color='black', linestyle='--')
    ax.axvline(5, color='black', linestyle='--')
    ax.set_xlabel(xlabel, fontsize=12, labelpad=15)
    ax.set_ylabel(ylabel, fontsize=12, labelpad=15)

    ax.set_xticks([2.5, 7.5]); ax.set_xticklabels(['Low', 'High'])
    ax.set_yticks([2.5, 7.5]); ax.set_yticklabels(['Low', 'High'])

    plt.title(title, fontsize=14, weight='bold', pad=20)
    plt.tight_layout()
    plt.savefig(filepath, bbox_inches='tight', dpi=150)
    plt.close()

def draw_flowchart(title, steps, filepath):
    """Draws a simple horizontal flowchart."""
    fig, ax = plt.subplots(figsize=(10, 3))
    ax.axis('off')
    ax.set_title(title, fontsize=14, weight='bold', pad=10)

    node_style = dict(boxstyle='round,pad=0.5', fc='skyblue', ec='black')
    arrow_style = dict(arrowstyle='->', connectionstyle='arc3', color='black', lw=2)
    positions = [(0.15, 0.5), (0.5, 0.5), (0.85, 0.5)]

    for i, step in enumerate(steps):
        ax.text(positions[i][0], positions[i][1], textwrap.fill(step, 18), ha='center', va='center', bbox=node_style, transform=ax.transAxes)
        if i > 0:
            ax.add_patch(FancyArrowPatch(
                (positions[i-1][0] + 0.1, 0.5), (positions[i][0] - 0.1, 0.5),
                transform=ax.transAxes, **arrow_style
            ))
    plt.savefig(filepath, bbox_inches='tight', dpi=150)
    plt.close()

def draw_fishbone(title, main_bone, categories, filepath):
    """Draws a fishbone (Ishikawa) diagram."""
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_title(title, fontsize=16, weight='bold', pad=20)
    ax.axis('off')
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)

    # Main bone
    ax.arrow(0.05, 0.5, 0.85, 0, head_width=0.03, head_length=0.03, fc='black', ec='black', length_includes_head=True)
    ax.text(0.95, 0.5, main_bone, ha='left', va='center', weight='bold', fontsize=14)

    # Categories
    num_cats = len(categories)
    top_positions = [(0.2, 0.7, -60), (0.4, 0.7, -60)]
    bottom_positions = [(0.6, 0.3, 60), (0.8, 0.3, 60)]
    positions = top_positions + bottom_positions

    for i, (category, causes) in enumerate(categories.items()):
        pos_x, pos_y, angle = positions[i]
        # Branch from main bone
        ax.plot([pos_x, pos_x], [0.5, pos_y], color='black')
        ax.text(pos_x, pos_y + 0.05 if pos_y > 0.5 else pos_y - 0.05, category, ha='center', va='bottom' if pos_y > 0.5 else 'top', weight='bold')

        # Causes
        for j, cause in enumerate(causes):
            ax.plot([pos_x - 0.1, pos_x], [pos_y, pos_y], 'k-') # Simple horizontal line for cause
            ax.text(pos_x - 0.12, pos_y, cause, ha='right', va='center')
            pos_y += 0.08 if pos_y < 0.5 else -0.08 # Shift next cause

    plt.savefig(filepath, bbox_inches='tight', dpi=150)
    plt.close()
    
def draw_venn2_diagram(title, label1, label2, overlap_text, unique1_text, unique2_text, filepath):
    """Draws a 2-circle Venn diagram."""
    plt.figure(figsize=(10, 6))
    v = venn2(subsets={'10': 1, '01': 1, '11': 1}, set_labels=(label1, label2))
    venn2_circles(subsets=(1, 1, 1), linestyle='-')
    
    # Customize text
    if v.get_label_by_id('10'): v.get_label_by_id('10').set_text(textwrap.fill(unique1_text, 20))
    if v.get_label_by_id('01'): v.get_label_by_id('01').set_text(textwrap.fill(unique2_text, 20))
    if v.get_label_by_id('11'): v.get_label_by_id('11').set_text(textwrap.fill(overlap_text, 15))
    for label in v.set_labels:
        if label: label.set_fontsize(14)
    for text in v.subset_labels:
        if text: text.set_fontsize(10)

    plt.title(title, fontsize=16, weight='bold')
    plt.savefig(filepath, bbox_inches='tight', dpi=150)
    plt.close()

def draw_conceptual_triangle(title, vertices, center_text, filepath):
    """Draws a triangle with labels at vertices and center."""
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.axis('off'); ax.set_title(title, fontsize=16, weight='bold', pad=20)
    p1, p2, p3 = (0.5, 0.9), (0.1, 0.1), (0.9, 0.1)
    
    # Draw triangle and labels
    ax.plot([p1[0], p2[0], p3[0], p1[0]], [p1[1], p2[1], p3[1], p1[1]], 'k-')
    ax.text(p1[0], p1[1]+0.05, vertices[0], ha='center', va='center', bbox=dict(fc='lightblue', pad=5))
    ax.text(p2[0]-0.05, p2[1], vertices[1], ha='right', va='center', bbox=dict(fc='lightgreen', pad=5))
    ax.text(p3[0]+0.05, p3[1], vertices[2], ha='left', va='center', bbox=dict(fc='lightcoral', pad=5))
    ax.text(0.5, 0.5, center_text, ha='center', va='center', weight='bold', fontsize=12, bbox=dict(fc='gold', boxstyle='circle,pad=0.5'))

    plt.savefig(filepath, bbox_inches='tight', dpi=150)
    plt.close()

# --- MAIN SCRIPT LOGIC ---

def main():
    """Main function to generate the PDF with diagrams."""
    print("--- Starting PDF Generation ---")
    setup_directories()

    pdf_path = os.path.join(OUTPUT_DIR, PDF_FILENAME)
    doc = SimpleDocTemplate(pdf_path, pagesize=A4, rightMargin=inch, leftMargin=inch, topMargin=inch, bottomMargin=inch)
    story = []

    # Setup styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle('TitleStyle', parent=styles['h1'], fontSize=18, spaceAfter=14, textColor=colors.HexColor('#2C3E50'))
    question_style = ParagraphStyle('QuestionStyle', parent=styles['h2'], fontSize=12, spaceAfter=10, leading=14, textColor=colors.HexColor('#34495E'))
    body_style = styles['BodyText']

    # Group questions by year for easier processing
    exams = {}
    for item in EXAM_DATA:
        year = item['year']
        if year not in exams:
            exams[year] = []
        exams[year].append(item)

    # Sort years to process them in order
    sorted_years = sorted(exams.keys())

    for year in sorted_years:
        story.append(Paragraph(f"Exam Solutions: {year}", title_style))
        story.append(Spacer(1, 0.5 * inch))

        for item in sorted(exams[year], key=lambda x: x['question_number']):
            q_num = item['question_number']
            print(f"Processing: Q{q_num} ({year})")
            
            story.append(Paragraph(item['question_text'], question_style))
            story.append(Spacer(1, 0.2 * inch))

            suggestion = item['diagram_suggestion']
            img_name = f"q{q_num}_{year.replace(' ', '_')}.png"
            img_path = os.path.join(IMG_DIR, img_name)
            
            numbered_title = f"Diagram for Q{q_num} ({year})"

            try:
                # =================== DIAGRAM GENERATION ROUTER ===================
                
                # --- June 2023 ---
                if year == 'June 2023' and q_num == 1:
                    numbered_title += ": DHRM vs IHRM & EPRG Framework"
                    create_table_image([
                        ['Parameter', 'Domestic HRM (DHRM)', 'International HRM (IHRM)'],
                        ['Scope', 'National', 'Global (Multiple Countries)'],
                        ['Activities', 'Standard HR Functions', 'Adds intl. tax, relocation, family support'],
                        ['Risk', 'Lower (e.g., legal compliance)', 'Higher (e.g., expat failure, political)'],
                    ], [0.2, 0.4, 0.4], numbered_title, img_path)

                elif year == 'June 2023' and q_num == 2:
                    numbered_title += ": MNC Competitive Strategies"
                    draw_2x2_matrix(numbered_title, "Pressure for Local Responsiveness", "Pressure for Global Integration",
                                     "Global Strategy\n(High Integration,\nLow Responsiveness)",
                                     "Transnational Strategy\n(High Integration,\nHigh Responsiveness)",
                                     "International Strategy\n(Low Integration,\nLow Responsiveness)",
                                     "Multidomestic Strategy\n(Low Integration,\nHigh Responsiveness)",
                                     "Regional\n(Mid-point)", img_path)
                
                elif year == 'June 2023' and q_num == 3:
                    numbered_title += ": International Assignment Training Timeline"
                    draw_flowchart(numbered_title,
                                   ['Pre-Departure\n(Cultural, Language,\nPractical Training)',
                                    'In-Country\n(Mentorship, Ongoing\nSupport, Coaching)',
                                    'Pre-Repatriation\n(Career Planning,\nReverse Culture Shock)'], img_path)

                elif year == 'June 2023' and q_num == 4:
                    numbered_title += ": Total Rewards & Taxation Challenges"
                    # Combined Diagram
                    fig = plt.figure(figsize=(12, 6)); fig.suptitle(numbered_title, fontsize=16, weight='bold')
                    ax1 = fig.add_subplot(1, 2, 1); ax1.set_title("Total Rewards System", pad=15)
                    ax1.pie([1, 1], labels=['Financial', 'Non-Financial'], colors=['#ff9999','#66b3ff'], autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.3, edgecolor='w'))
                    ax1.add_artist(plt.Circle((0,0),0.70,fc='white')); ax1.axis('equal')
                    ax2 = fig.add_subplot(1, 2, 2); ax2.set_title("Intl. Taxation Challenges", pad=15); ax2.axis('off')
                    ax2.text(0.1, 0.6, 'Home Country', ha='center', bbox=dict(fc='lightgreen')); ax2.text(0.9, 0.6, 'Host Country', ha='center', bbox=dict(fc='lightblue'))
                    ax2.annotate('Double Tax Liability', xy=(0.7, 0.6), xytext=(0.3, 0.6), arrowprops=dict(arrowstyle='<->', color='red'))
                    plt.tight_layout(rect=[0, 0.03, 1, 0.95]); plt.savefig(img_path, bbox_inches='tight', dpi=150); plt.close()

                elif year == 'June 2023' and q_num == 5:
                    numbered_title += ": Motivation Theories in an International Context"
                    table_data = [
                        ['Theory', 'Key Tenets', 'Cross-Cultural Considerations'],
                        ['Maslow\'s Hierarchy', 'Needs are hierarchical', 'Hierarchy & salience of needs can vary culturally.'],
                        ['Herzberg\'s Two-Factor', 'Hygiene vs. Motivator factors', 'What constitutes a motivator is culturally dependent.'],
                        ['Expectancy Theory', 'Effort -> Performance -> Reward', 'Valence of rewards is culturally influenced.'],
                        ['Equity Theory', 'Fair input/output ratio vs. others', 'Concept of fairness and comparison group varies.']
                    ]
                    create_table_image(table_data, [0.15, 0.35, 0.5], numbered_title, img_path)

                elif year == 'June 2023' and q_num == 6:
                    numbered_title += ": Relationship between HPWS and HPO"
                    fig, ax = plt.subplots(figsize=(10, 5)); ax.axis('off'); ax.set_title(numbered_title, fontsize=16, weight='bold')
                    hpws_items = "Inputs (HPWS):\n• Selective Hiring\n• Empowerment\n• Info Sharing"
                    ax.text(0.2, 0.5, hpws_items, ha='center', va='center', bbox=dict(boxstyle='round', fc='lightblue', pad=10))
                    ax.annotate("", xy=(0.7, 0.5), xytext=(0.4, 0.5), arrowprops=dict(arrowstyle="=>", mutation_scale=30, lw=3))
                    hpo_items = "Outcomes (HPO):\n• Superior Results\n• Adaptability\n• Innovation"
                    ax.text(0.8, 0.5, hpo_items, ha='center', va='center', bbox=dict(boxstyle='round', fc='lightgreen', pad=10))
                    plt.savefig(img_path, bbox_inches='tight', dpi=150); plt.close()
                
                elif year == 'June 2023' and q_num == 7:
                    numbered_title += ": Role of Employer's Associations"
                    fig, ax = plt.subplots(figsize=(10, 7)); ax.axis('off'); ax.set_title(numbered_title, fontsize=16, weight='bold')
                    ax.text(0.5, 0.1, 'MNC', ha='center', bbox=dict(fc='gold', pad=5))
                    ax.text(0.2, 0.4, "Host Country Environment", ha='center', bbox=dict(fc='lightgrey'))
                    ax.text(0.8, 0.4, "National Employer\nAssociation", ha='center', bbox=dict(fc='lightgrey'))
                    ax.text(0.5, 0.7, "International Employer Association", ha='center', bbox=dict(fc='lightblue'))
                    ax.text(0.5, 0.9, "Supranational Bodies\n(EU, ILO, OECD)", ha='center', bbox=dict(fc='lightgreen'))
                    plt.savefig(img_path, bbox_inches='tight', dpi=150); plt.close()

                elif year == 'June 2023' and q_num == 8:
                    numbered_title += ": IHRM Trends, Challenges, and Strategies"
                    fig, ax = plt.subplots(figsize=(10, 8)); ax.axis('off'); ax.set_title(numbered_title, fontsize=16, weight='bold')
                    ax.text(0.5, 0.5, "IHRM", ha='center', va='center', bbox=dict(boxstyle='circle', fc='gold', pad=10))
                    ax.text(0.1, 0.8, "Trends:\n- Globalization\n- Tech", ha='center', bbox=dict(fc='lightblue'))
                    ax.text(0.9, 0.8, "Challenges:\n- Culture\n- Talent Mgt.", ha='center', bbox=dict(fc='lightcoral'))
                    ax.text(0.5, 0.1, "Strategies:\n- Global Mindset\n- Leverage Tech", ha='center', bbox=dict(fc='lightgreen'))
                    plt.savefig(img_path, bbox_inches='tight', dpi=150); plt.close()

                # --- June 2024 ---
                elif year == 'June 2024' and q_num == 1:
                    numbered_title += ": DHRM vs. IHRM"
                    draw_venn2_diagram(numbered_title, "DHRM", "IHRM",
                                        "Core HR Functions\n(Recruit, Train, etc.)",
                                        "• Single National Context\n• Lower Risk & Complexity",
                                        "• Multiple Countries\n• Additional Activities (Tax)\n• Higher Risk & Complexity",
                                        img_path)

                elif year == 'June 2024' and q_num == 2:
                    numbered_title += ": Cultural Differences"
                    table_data = [
                        ['Aspect', 'Individualistic Society', 'Collectivist Society'],
                        ['Self-Concept', "'I' identity, personal uniqueness", "'We' identity, group membership"],
                        ['Goals', 'Personal achievement, self-interest', 'Group goals, harmony, loyalty'],
                        ['Relationships', 'Loose ties, nuclear family focus', 'Strong, cohesive in-groups'],
                    ]
                    create_table_image(table_data, [0.2, 0.4, 0.4], numbered_title, img_path)
                    
                elif year == 'June 2024' and q_num == 3:
                    numbered_title += ": Reasons for Expatriate Failure"
                    draw_fishbone(numbered_title, "Expat Failure",
                                  {
                                      'Individual Factors': ['Inability to Adapt', 'Immaturity'],
                                      'Family Factors': ['Spouse cannot adjust', 'Isolation'],
                                      'Organizational Factors': ['Poor Selection', 'Inadequate Training'],
                                      'Host Country Factors': ['Lack of Support', 'Cultural Toughness']
                                  }, img_path)

                elif year == 'June 2024' and q_num == 4:
                    numbered_title += ": Expatriate Goal Assessment Model"
                    draw_conceptual_triangle(numbered_title,
                                             ['Hard Goals\n(Quantitative)', 'Soft Goals\n(Behavioral)', 'Contextual Goals\n(Situational)'],
                                             "Overall\nManagerial\nPerformance",
                                             img_path)

                elif year == 'June 2024' and q_num == 5:
                    numbered_title += ": Leadership Comparison"
                    draw_venn2_diagram(numbered_title, "Leadership in France", "Leadership in Arab World",
                                        "• Hierarchical\n• Centralized",
                                        "• Emphasis on Intellect\n• Formal Communication",
                                        "• Paternalism\n• Personalism/Kinship",
                                        img_path)

                # --- December 2023 ---
                elif year == 'December 2023' and q_num == 1:
                    numbered_title += ": Cultural Models & Dynamics"
                    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6)); fig.suptitle(numbered_title, fontsize=16, weight='bold')
                    # Onion Model
                    ax1.set_title("Hofstede's Onion Model"); ax1.set_aspect('equal'); ax1.axis('off')
                    layers = [('Values', 0.2), ('Rituals', 0.4), ('Heroes', 0.6), ('Symbols', 0.8)]
                    for name, radius in reversed(layers):
                        ax1.add_patch(Circle((0.5, 0.5), radius, fill=False, ec='black'))
                        ax1.text(0.5, 0.5 + radius - 0.1, name, ha='center')
                    # Convergence/Divergence
                    ax2.set_title("Convergence vs. Divergence"); ax2.axis('off')
                    ax2.add_patch(Circle((0.3, 0.5), 0.2, fc='lightblue', alpha=0.6)); ax2.text(0.3, 0.5, "Culture A", ha='center')
                    ax2.add_patch(Circle((0.7, 0.5), 0.2, fc='lightgreen', alpha=0.6)); ax2.text(0.7, 0.5, "Culture B", ha='center')
                    ax2.arrow(0.4, 0.7, 0.2, 0, head_width=0.05, color='red'); ax2.arrow(0.6, 0.3, -0.2, 0, head_width=0.05, color='red')
                    ax2.text(0.5, 0.8, "Convergence", ha='center'); ax2.text(0.5, 0.2, "(Globalization)", ha='center', style='italic')
                    plt.savefig(img_path, bbox_inches='tight', dpi=150); plt.close()

                elif year == 'December 2023' and q_num == 2:
                    numbered_title += ": Expatriate Failure Reasons & Solutions"
                    draw_fishbone(numbered_title, "Expat Failure",
                        {
                            'Poor Selection': [], 'Family Issues': [], 
                            'Cultural Inadaptability': [], 'Lack of Training': []
                        }, img_path)

                elif year == 'December 2023' and q_num == 3:
                    numbered_title += ": Balanced Scorecard for IPM"
                    draw_2x2_matrix(numbered_title, "Task-Focused ('What')", "Behavior-Focused ('How')",
                                   "Contextual Criteria\n(Navigating local challenges)", "Developmental Criteria\n(Learning, skill growth)",
                                   "Hard Criteria\n(KPIs, sales, profit)", "Soft Criteria\n(Leadership, teamwork)",
                                   None, img_path)

                else:
                    raise NotImplementedError(f"No specific diagram logic for Q{q_num} ({year}).")
                
                img = Image(img_path, width=7*inch, height=5*inch, kind='proportional')
                story.append(img)

            except Exception as e:
                print(f"  -> ERROR generating diagram for Q{q_num} ({year}): {e}")
                story.append(Paragraph(f"[Error creating diagram: {e}]", body_style))
            
            story.append(PageBreak())

    # Build the PDF
    try:
        doc.build(story)
        print(f"\n--- PDF Generation Complete ---")
        print(f"Successfully saved to: {pdf_path}")
    except Exception as e:
        print(f"\n--- PDF GENERATION FAILED ---")
        print(f"Error: {e}")
    finally:
        cleanup_directories()
        print("Temporary files cleaned up.")


if __name__ == '__main__':
    main()
