import os
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib import colors
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import A4
import traceback # For error reporting

# --- Configuration ---
# !! IMPORTANT: Make sure this path exists and is writable !!
OUTPUT_DIR = "/storage/emulated/0/Download"
OUTPUT_FILENAME = os.path.join(OUTPUT_DIR, "Survey_Analysis_Report_Final_1_to_20.pdf")
CHART_DIR = os.path.join(OUTPUT_DIR, "charts_temp_final") # Temporary dir for chart images

# Ensure the output and chart directories exist
try:
    if not os.path.exists(OUTPUT_DIR):
        print(f"Warning: Output directory {OUTPUT_DIR} does not exist. Attempting to create.")
        os.makedirs(OUTPUT_DIR)
    if not os.path.exists(CHART_DIR):
        os.makedirs(CHART_DIR)
    print(f"Output will be saved to: {OUTPUT_FILENAME}")
    print(f"Temporary charts will be saved in: {CHART_DIR}")
except Exception as e:
    print(f"Error creating directories: {e}")
    print("Please ensure the path is correct and you have write permissions.")
    exit()

# --- Data and Interpretations (Questions 1-20) ---
survey_data = [
    # --- Section A: Demographic Profile ---
    {
        "question_num": 1,
        "question_text": "Age",
        "data": {
            "Under 25": 5,
            "26-35": 30,
            "36-45": 35,
            "46-55": 20,
            "Above 55": 10,
        },
        "chart_type": "pie",
        "interpretation": "The age distribution of individuals in this dataset offers valuable insights into the composition of the population, particularly regarding the potential preferences, needs, and motivations of different age groups. The largest proportion of people falls within the 36–45 age group, accounting for 35% of the total, followed closely by those in the 26–35 range (30%). Individuals aged 46–55 make up 20%, while those above 55 and under 25 represent smaller segments, each comprising 10% and 5% respectively."
    },
    {
        "question_num": 2,
        "question_text": "Gender",
        "data": {
            "Male": 58,
            "Female": 42,
        },
        "chart_type": "pie",
        "interpretation": "The respondent pool shows a slight male majority, with men constituting 58% and women 42% of the participants. This distribution suggests that while both genders are represented, insights might be slightly more reflective of male customer perspectives within this specific sample from the Kollam District."
    },
    {
        "question_num": 3,
        "question_text": "Occupation",
        "data": {
            "Student": 10,
            "Salaried": 45,
            "Business": 20,
            "Retired": 15,
            "Others": 10,
        },
        "chart_type": "pie",
        "interpretation": "Salaried individuals form the largest segment of respondents at 45%, indicating that employed professionals are a significant customer base for ICICI Prudential in this survey. Business owners (20%) and retired individuals (15%) also represent substantial portions, while students and 'Others' constitute smaller groups (10% each)."
    },
    {
        "question_num": 4,
        "question_text": "Duration of association with ICICI Prudential",
        "data": {
            "Less than 1 year": 25,
            "1-3 years": 25,
            "3-5 years": 20,
            "More than 5 years": 30,
        },
        "chart_type": "pie",
        "interpretation": "The customer tenure is varied. While the largest single group (30%) consists of long-term customers associated for more than 5 years, there is a significant presence of newer customers, with those associated for less than 1 year and 1-3 years each accounting for 25%. This indicates a mix of established loyalty and recent customer acquisition."
    },
    {
        "question_num": 5,
        "question_text": "Type of policy held",
        "data": {
            "Life Insurance": 5,
            "ULIP": 50,
            "Term Plan": 20,
            "Health Insurance": 5,
            "Others (Traditional Plan)": 20,
        },
        "chart_type": "pie",
        "interpretation": "Unit Linked Insurance Plans (ULIPs) are the dominant policy type held by respondents, accounting for 50% of the sample. Term Plans and 'Others' (specified as Traditional Plans) each represent 20%, while standard Life Insurance and Health Insurance are held by smaller proportions (5% each), highlighting the strong preference or push for ULIPs among this group."
    },
    # --- Section B: Customer Engagement ---
    {
        "question_num": 6,
        "question_text": "How often does ICICI Prudential communicate with you?",
        "data": {
            "Very Frequently": 50,
            "Frequently": 20,
            "Occasionally": 10,
            "Rarely": 5,
            "Never": 15,
        },
        "chart_type": "pie",
        "interpretation": "A significant majority of customers report frequent contact, with 50% stating communication is 'Very Frequent' and another 20% 'Frequent'. However, there's a notable group (15%) who report 'Never' receiving communication, suggesting inconsistencies in outreach efforts or channel effectiveness."
    },
    {
        "question_num": 7,
        "question_text": "Through which channels do you receive communication from ICICI Prudential? (Select all that apply)",
        "data": {
            "SMS": 10,
            "Email": 35,
            "Phone Calls": 45,
            "In-person Meetings": 5,
            "Mobile App": 5,
        },
        "chart_type": "bar", # Use bar chart for multi-select
        "interpretation": "Phone calls (45%) and Email (35%) emerge as the primary communication channels experienced by customers. Lower engagement is reported via SMS (10%), In-person Meetings (5%), and the Mobile App (5%), indicating a reliance on more traditional direct outreach methods. (Note: Percentages reflect the portion of 100 respondents selecting each option)."
    },
    {
        "question_num": 8,
        "question_text": "How satisfied are you with the communication you receive from ICICI Prudential?",
        "data": {
            "Very Satisfied": 20,
            "Satisfied": 30,
            "Neutral": 30,
            "Dissatisfied": 10,
            "Very Dissatisfied": 10,
        },
        "chart_type": "pie",
        "interpretation": "Customer satisfaction with communication is moderate. Half the respondents are 'Satisfied' (30%) or 'Very Satisfied' (20%). However, a large segment (30%) remains 'Neutral', and a combined 20% express dissatisfaction ('Dissatisfied' 10%, 'Very Dissatisfied' 10%), pointing towards potential areas for improving communication relevance and quality."
    },
    {
        "question_num": 9,
        "question_text": "How helpful is the customer service/support of ICICI Prudential?",
        "data": {
            "Very Helpful": 10,
            "Helpful": 45,
            "Neutral": 20,
            "Not Helpful": 20,
            "Very Poor": 5,
        },
        "chart_type": "pie",
        "interpretation": "A slight majority finds the customer service helpful, with 45% deeming it 'Helpful' and 10% 'Very Helpful'. Nevertheless, a significant portion remains unconvinced, including 20% 'Neutral', 20% finding it 'Not Helpful', and 5% 'Very Poor', indicating inconsistency in service experience."
    },
    {
        "question_num": 10,
        "question_text": "Do you feel valued as a customer of ICICI Prudential?",
        "data": {
            "Strongly Agree": 5,
            "Agree": 45,
            "Neutral": 25,
            "Disagree": 18,
            "Strongly Disagree": 7,
        },
        "chart_type": "pie",
        "interpretation": "Perceptions of feeling valued are mixed. Half the respondents 'Agree' (45%) or 'Strongly Agree' (5%) that they feel valued. Conversely, 25% are 'Neutral', and another 25% 'Disagree' (18%) or 'Strongly Disagree' (7%), suggesting that a substantial part of the customer base does not feel particularly appreciated."
    },
    # --- Section C: Customer Loyalty ---
    {
        "question_num": 11,
        "question_text": "How likely are you to renew your current policy with ICICI Prudential?",
        "data": {
            "Very Likely": 18,
            "Likely": 50,
            "Not Sure": 10,
            "Unlikely": 15,
            "Very Unlikely": 7,
        },
        "chart_type": "pie",
        "interpretation": "Renewal intentions appear strong, with a majority of respondents indicating they are 'Likely' (50%) or 'Very Likely' (18%) to renew their policies. While 10% are 'Not Sure', a combined 22% lean towards not renewing ('Unlikely' 15%, 'Very Unlikely' 7%), showing generally positive retention prospects but also a segment at risk of attrition."
    },
    {
        "question_num": 12,
        "question_text": "Would you consider switching to another insurance company in the future?",
        "data": {
            "Definitely Yes": 7,
            "Probably Yes": 15,
            "Not Sure": 10,
            "Probably Not": 50,
            "Definitely Not": 18,
        },
        "chart_type": "pie",
        "interpretation": "Customer retention appears relatively robust, as a significant majority state they would 'Probably Not' (50%) or 'Definitely Not' (18%) consider switching. However, 22% ('Probably Yes' 15%, 'Definitely Yes' 7%) are open to switching, indicating potential vulnerability to competitors despite overall loyalty."
    },
    {
        "question_num": 13,
        "question_text": "Do you recommend ICICI Prudential to friends and family?",
        "data": {
            "Frequently": 20,
            "Occasionally": 20,
            "Rarely": 50,
            "Never": 10,
        },
        "chart_type": "pie",
        "interpretation": "Customer advocacy is weak among this group. The largest segment (50%) 'Rarely' recommends the company, and 10% 'Never' do. Only 40% recommend 'Frequently' (20%) or 'Occasionally' (20%), suggesting that while customers may stay, they are not strong promoters of the brand."
    },
     {
        "question_num": 14,
        "question_text": "How satisfied are you with the overall services of ICICI Prudential?",
        "data": {
            "Very Satisfied": 10,
            "Satisfied": 30,
            "Neutral": 50,
            "Dissatisfied": 15,
            "Very Dissatisfied": 5,
        },
        "chart_type": "pie",
        "interpretation": "Overall satisfaction is lukewarm, dominated by a large 'Neutral' group (50%). While 40% express satisfaction ('Satisfied' 30%, 'Very Satisfied' 10%), a notable 20% are dissatisfied ('Dissatisfied' 15%, 'Very Dissatisfied' 5%). This suggests a lack of strong positive experiences for many customers."
    },
    {
        "question_num": 15,
        "question_text": "Has your trust in ICICI Prudential increased over time?",
        "data": {
            "Strongly Agree": 10,
            "Agree": 30,
            "Neutral": 30,
            "Disagree": 20,
            "Strongly Disagree": 10,
        },
        "chart_type": "pie",
        "interpretation": "Views on whether trust has increased are divided. While 40% 'Agree' (30%) or 'Strongly Agree' (10%) that trust has grown, 30% are 'Neutral', and another 30% 'Disagree' (20%) or 'Strongly Disagree' (10%). This suggests inconsistent experiences in building deeper customer trust over the duration of the relationship."
    },
    # --- Section D: Customer Retention ---
    {
        "question_num": 16,
        "question_text": "What is the main reason for staying with ICICI Prudential?",
        "data": {
            "Service Quality": 20,
            "Policy Benefits": 30,
            "Trust/Brand Name": 40,
            "Customer Support": 10,
        },
         "chart_type": "pie",
        "interpretation": "The primary retention driver cited is 'Trust/Brand Name' (40%), followed closely by 'Policy Benefits' (30%). 'Service Quality' (20%) and 'Customer Support' (10%) are mentioned less frequently, indicating that the company's reputation and product offerings are more influential in retaining these customers than the service experience itself."
    },
    {
        "question_num": 17,
        "question_text": "How likely are you to purchase additional policies from ICICI Prudential?",
        "data": {
            "Very Likely": 20,
            "Likely": 35,
            "Not Sure": 20,
            "Unlikely": 18,
            "Very Unlikely": 7,
        },
        "chart_type": "pie",
        "interpretation": "There is moderate potential for cross-selling or up-selling, with 55% of respondents indicating they are 'Likely' (35%) or 'Very Likely' (20%) to purchase additional policies. However, 20% are 'Not Sure', and a quarter ('Unlikely' 18%, 'Very Unlikely' 7%) show reluctance towards further purchases."
    },
    {
        "question_num": 18,
        "question_text": "Do you feel the company understands your financial goals?",
        "data": {
            "Strongly Agree": 20,
            "Agree": 30,
            "Neutral": 20,
            "Disagree": 20,
            "Strongly Disagree": 10,
        },
        "chart_type": "pie",
        "interpretation": "Perception is split regarding whether ICICI Prudential understands customer financial goals. Exactly half 'Agree' (30%) or 'Strongly Agree' (20%). The remaining half is divided between 'Neutral' (20%) and those who 'Disagree' (20%) or 'Strongly Disagree' (10%), highlighting a gap in personalized understanding for many clients."
    },
    {
        "question_num": 19,
        "question_text": "Has your experience improved with ICICI Prudential over the years?",
        "data": {
            "Yes, significantly": 50,
            "Yes, somewhat": 20,
            "No change": 20,
            "No, it has worsened": 10,
        },
        "chart_type": "pie",
        "interpretation": "A strong majority (70%) perceive an improvement in their experience, reporting it has improved 'significantly' (50%) or 'somewhat' (20%). While 20% noted 'No change', only 10% felt the experience has 'worsened', suggesting positive evolution in customer interactions over time for most respondents."
    },
    # --- Open-ended Question (No Table/Chart) ---
     {
        "question_num": 20,
        "question_text": "In your opinion, what should ICICI Prudential improve to enhance your loyalty? (Open-ended response)",
        # No 'data' key as it's qualitative. Table/chart generation will be skipped.
        "interpretation": "The qualitative feedback suggests customers desire improvements in personalized service and transparency. Key recommendations include better understanding of individual needs for tailored plan suggestions, clearer explanations of policy terms, hidden clauses, and charges by agents/staff, and reducing the frequency of potentially intrusive sales calls."
    },
]

# --- Styling ---
styles = getSampleStyleSheet()
style_title = styles['h2']
style_title.alignment = TA_LEFT
style_title.fontName = 'Helvetica-Bold'
style_title.fontSize = 12
style_title.spaceAfter = 6

style_body = styles['BodyText']
style_body.alignment = TA_LEFT
style_body.fontName = 'Helvetica'
style_body.fontSize = 10
style_body.leading = 14
style_body.spaceAfter = 6

style_interpretation_title = Paragraph("<b>Interpretation</b>", style_body)

# Table Styling - Reverted to the "professional" grey/beige style
table_style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),           # Header background
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),      # Header text
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 10),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 8),

    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),       # Body background
    ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),         # Body text
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 1), (-1, -1), 9),
    ('ALIGN', (0, 1), (-1, -1), 'CENTER'),                 # Center align text in cells
    ('TOPPADDING', (0, 1), (-1, -1), 4),
    ('BOTTOMPADDING', (0, 1), (-1, -1), 4),

    # Grid lines
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    # Style for TOTAL row (last row index is -1)
    ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
    ('BACKGROUND', (0, -1), (-1, -1), colors.lightgrey),   # Different background for Total row
])


# Chart and Spacer settings
chart_width = 4.5 * inch
chart_height = chart_width * 0.7
spacer_small = Spacer(1, 0.2 * inch)
spacer_medium = Spacer(1, 0.3 * inch)

# --- Chart Generation Function ---
def create_chart(data_dict, total_respondents, chart_type, filename, title_prefix):
    """Generates and saves a 2D pie or bar chart.
       Note: 3D Pie charts are not generated due to complexity and visualization concerns.
    """
    labels = list(data_dict.keys())
    counts = list(data_dict.values())

    # Define color palette
    num_colors = len(labels)
    cmap = plt.get_cmap('tab10') # Using a standard, clear colormap
    chart_colors = [cmap(i % cmap.N) for i in range(num_colors)]

    plt.figure(figsize=(6, 4))

    if chart_type == 'pie':
        # Ensure total_respondents is not zero for percentage calculation
        calc_total = total_respondents if total_respondents > 0 else 1
        percentages = [(count / calc_total) * 100 for count in counts]
        legend_labels = [f'{l} ({c})' for l, c in zip(labels, counts)]
        explode_values = [0.01] * len(labels) # Slight separation

        wedges, texts, autotexts = plt.pie(
            percentages,
            autopct='%1.1f%%',
            startangle=90,
            colors=chart_colors,
            pctdistance=0.85,
            explode=explode_values,
            wedgeprops={'edgecolor': 'black', 'linewidth': 0.5} # Edge for clarity
        )
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontsize(8)
            autotext.set_fontweight('bold')

        plt.legend(wedges, legend_labels, title="Categories", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=8)
        plt.axis('equal')

    elif chart_type == 'bar':
        # Ensure total_respondents is not zero
        calc_total = total_respondents if total_respondents > 0 else 1
        percentages = [(count / calc_total) * 100 for count in counts]
        bars = plt.bar(labels, percentages, color=chart_colors)
        plt.ylabel('Percentage of Respondents (%)', fontsize=9)
        plt.xticks(rotation=20, ha='right', fontsize=8)
        plt.yticks(fontsize=8)
        plt.ylim(0, max(percentages or [0]) * 1.15)
        plt.grid(axis='y', linestyle='--', alpha=0.6)

        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2.0, yval, f'{yval:.1f}%', va='bottom', ha='center', fontsize=8)

    else:
        print(f"Warning: Unknown chart type '{chart_type}' for Q{title_prefix}. Skipping chart.")
        plt.close()
        return None

    plt.tight_layout(rect=[0, 0, 0.80, 1] if chart_type=='pie' else None)
    try:
        plt.savefig(filename, format='png', dpi=300, bbox_inches='tight')
        print(f"Chart saved: {filename}")
    except Exception as e:
        print(f"Error saving chart {filename}: {e}")
        filename = None
    finally:
        plt.close()

    return filename

# --- PDF Generation ---
doc = SimpleDocTemplate(OUTPUT_FILENAME, pagesize=A4,
                        leftMargin=0.8*inch, rightMargin=0.8*inch,
                        topMargin=0.8*inch, bottomMargin=0.8*inch)
story = []

print(f"\nStarting PDF generation (No Title Page)...")

for item in survey_data:
    q_num = item['question_num']
    q_text = item['question_text']
    q_interpretation = item['interpretation']

    print(f"Processing Question {q_num}: {q_text[:50]}...")

    # 1. Title
    title_text = f"{q_num}. {q_text}"
    story.append(Paragraph(title_text, style_title))

    # Check if data exists for table and chart generation
    # This will correctly skip Q20 which lacks the 'data' key
    if 'data' in item and item['data']:
        q_data = item['data']
        q_chart_type = item['chart_type']

        # 2. Table Data
        table_data = [['CATEGORY', 'NUMBER OF PERSONS', 'PERCENTAGE']]
        total_count = sum(q_data.values())
        total_respondents = 100 # Assume 100 total respondents for base % calc if needed

        # Determine denominator for percentage calculation
        perc_basis = total_count if q_chart_type == 'pie' else total_respondents
        # Avoid division by zero
        if perc_basis == 0: perc_basis = 1

        for category, count in q_data.items():
            percentage = (count / perc_basis) * 100
            # Use Paragraph for category cell to allow wrapping
            table_data.append([
                Paragraph(str(category), style_body), # Ensure category is string
                str(count),
                f"{percentage:.1f}%"
            ])

        # Add Total Row only for pie charts
        if q_chart_type == 'pie':
             # Ensure total_count is used for the display, but percentage is 100%
             table_data.append(['TOTAL', str(total_count), '100.0%'])

        # 3. Create and Add Table
        try:
            # Adjust column widths as needed for the new style/content
            table = Table(table_data, colWidths=[2.8*inch, 1.4*inch, 1.3*inch])
            # Apply the "professional" style reverted from earlier version
            table.setStyle(table_style)
            story.append(table)
            story.append(spacer_medium)
        except Exception as e:
            print(f"Error creating table for Q{q_num}: {e}")
            story.append(Paragraph(f"[Error creating table for Q{q_num}]", style_body))


        # 4. Generate and Add Chart
        chart_filename = os.path.join(CHART_DIR, f"chart_q{q_num}.png")
        chart_title_prefix = f"{q_num}"
        generated_chart_path = create_chart(q_data, total_respondents, q_chart_type, chart_filename, chart_title_prefix)

        if generated_chart_path and os.path.exists(generated_chart_path):
            try:
                img = Image(generated_chart_path, width=chart_width, height=chart_height)
                img.hAlign = 'CENTER'
                story.append(img)
                story.append(spacer_medium)
            except Exception as e:
                 print(f"Error adding chart image for Q{q_num}: {e}")
                 story.append(Paragraph(f"[Error adding chart image for Q{q_num}]", style_body))
        else:
            print(f"Chart generation/finding failed for Q{q_num}")
            story.append(Paragraph(f"[Chart for Q{q_num} could not be generated/found]", style_body))
            story.append(spacer_medium)

    # 5. Interpretation (Always add interpretation)
    story.append(style_interpretation_title) # Add "Interpretation" heading
    story.append(Paragraph(q_interpretation, style_body)) # Add the text
    # Add Page Break unless it's the very last item
    if q_num < len(survey_data):
        story.append(PageBreak())


# --- Build the PDF ---
try:
    print("\nBuilding PDF document...")
    doc.build(story)
    print("-" * 40)
    print(" PDF GENERATION COMPLETE! ")
    print(f" File saved to: {OUTPUT_FILENAME}")
    print("-" * 40)
    # Optional cleanup: uncomment if needed
    # print("Cleaning up temporary chart files...")
    # ... (cleanup code) ...

except Exception as e:
    print(f"\n--- PDF GENERATION FAILED ---")
    print(f"An error occurred: {e}")
    traceback.print_exc()
    print("-" * 30)
