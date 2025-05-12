#!/usr/bin_env python3
# -*- coding: UTF-8 -*-

import os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch, cm
from reportlab.lib.colors import black, HexColor

def generate_exam_solutions_pdf():
    # Path for mobile. Change if running on PC.
    # Ensure the directory exists if it's a specific path.
    # For simplicity, let's try to save in the current directory if the mobile path fails.
    file_name = "MMPC_018_Solutions.pdf"
    mobile_path = "/storage/emulated/0/Download/"
    
    if os.path.exists(mobile_path) and os.path.isdir(mobile_path):
        output_path = os.path.join(mobile_path, file_name)
    else:
        print(f"Warning: Path '{mobile_path}' not found or not a directory. Saving to current directory.")
        output_path = file_name

    doc = SimpleDocTemplate(output_path, pagesize=A4,
                            rightMargin=2*cm, leftMargin=2*cm,
                            topMargin=2*cm, bottomMargin=2*cm)
    
    styles = getSampleStyleSheet()
    
    # Custom Styles
    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['h1'],
        fontSize=18,
        spaceAfter=0.5*cm,
        alignment=TA_CENTER,
        textColor=HexColor('#000080') # Dark Blue
    )
    
    question_style = ParagraphStyle(
        'QuestionStyle',
        parent=styles['h2'],
        fontSize=14,
        spaceBefore=0.8*cm,
        spaceAfter=0.3*cm,
        textColor=HexColor('#4682B4') # Steel Blue
    )
    
    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontSize=12,
        leading=16, # Line spacing
        alignment=TA_JUSTIFY,
        spaceAfter=0.2*cm
    )
    
    bold_point_style = ParagraphStyle(
        'BoldPointStyle',
        parent=body_style,
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        leftIndent=0.5*cm,
        bulletIndent=0*cm,
        spaceBefore=0.1*cm,
        spaceAfter=0.1*cm
    )

    sub_heading_style = ParagraphStyle(
        'SubHeadingStyle',
        parent=styles['h3'],
        fontSize=13,
        fontName='Helvetica-Bold',
        spaceBefore=0.3*cm,
        spaceAfter=0.2*cm,
        textColor=HexColor('#2F4F4F') # Dark Slate Gray
    )

    memory_trick_style = ParagraphStyle(
        'MemoryTrickStyle',
        parent=body_style,
        textColor=HexColor('#800080'), # Purple
        fontName='Helvetica-Oblique', # Italic
        leftIndent=0.5*cm,
        spaceBefore=0.2*cm,
        spaceAfter=0.3*cm
    )

    diagram_suggestion_style = ParagraphStyle(
        'DiagramSuggestionStyle',
        parent=body_style,
        textColor=HexColor('#006400'), # Dark Green
        leftIndent=0.5*cm,
        spaceBefore=0.2*cm,
        spaceAfter=0.3*cm
    )

    expand_points_style = ParagraphStyle(
        'ExpandPointsStyle',
        parent=body_style,
        fontName='Helvetica-BoldOblique',
        textColor=HexColor('#A0522D'), # Sienna
        spaceBefore=0.3*cm,
        spaceAfter=0.4*cm
    )

    story = []

    # Title
    story.append(Paragraph("MMPC-018: ENTREPRENEURSHIP - Exam Solutions (June 2023)", title_style))
    story.append(Spacer(1, 0.5*cm))

    # --- Question 1 ---
    story.append(Paragraph("1. Briefly trace the evolution of entrepreneurship from various schools of thoughts.", question_style))
    
    story.append(Paragraph("<u>Introduction:</u>", sub_heading_style))
    story.append(Paragraph("Entrepreneurship, the dynamic process of creating and managing a new venture, has evolved significantly in its conceptual understanding. Various schools of thought have contributed to shaping our perception of who an entrepreneur is and what entrepreneurship entails. Tracing this evolution helps in appreciating the multifaceted nature of this field.", body_style))

    story.append(Paragraph("<u>Evolution of Entrepreneurship - Schools of Thought:</u>", sub_heading_style))

    story.append(Paragraph("The understanding of entrepreneurship has progressed through several dominant perspectives:", body_style))

    story.append(Paragraph("1. The Economic School of Thought:", sub_heading_style))
    story.append(Paragraph("This is one of the earliest perspectives, focusing on the economic functions and contributions of the entrepreneur.", body_style))
    story.append(Paragraph("• <b>Richard Cantillon (Early 18th Century):</b> Often credited as one of the first to deeply analyze the entrepreneur. He viewed entrepreneurs as risk-takers who buy at certain prices and sell at uncertain prices, thereby bearing non-insurable risk. Jargon: 'Risk-bearer' – someone who accepts the possibility of loss in pursuit of profit.", bold_point_style))
    story.append(Paragraph("• <b>Jean-Baptiste Say (Early 19th Century):</b> Expanded on Cantillon's ideas. Say emphasized the entrepreneur's role as a coordinator of the factors of production (land, labor, capital). He shifted the focus from mere risk-bearing to the active management and combination of resources to create value.", bold_point_style))
    story.append(Paragraph("• <b>Joseph Schumpeter (Early to Mid-20th Century):</b> Perhaps the most influential economist in entrepreneurship theory. Schumpeter defined the entrepreneur as an innovator who drives 'creative destruction.' This involves introducing new products, new methods of production, new markets, new sources of supply, or new organizational structures. For Schumpeter, the entrepreneur was the engine of economic development, disrupting equilibrium to create new opportunities. Jargon: 'Creative Destruction' – the process of industrial mutation that incessantly revolutionizes the economic structure from within, destroying the old one, incessantly creating a new one.", bold_point_style))
    story.append(Paragraph("• <b>Frank Knight (Early 20th Century):</b> Differentiated between risk (measurable uncertainty) and true uncertainty (unmeasurable). Knight argued that entrepreneurs earn profits for dealing with true uncertainty, which cannot be insured against.", bold_point_style))
    story.append(Paragraph("• <b>Israel Kirzner (Late 20th Century):</b> Presented the entrepreneur as an 'alert' individual who discovers and exploits opportunities for profit that others have not noticed. This perspective focuses on market equilibrium and the entrepreneur's role in moving markets towards it by identifying and correcting inefficiencies.", bold_point_style))

    story.append(Paragraph("2. The Psychological School of Thought:", sub_heading_style))
    story.append(Paragraph("This school focuses on the personality traits, characteristics, and motivations of entrepreneurs.", body_style))
    story.append(Paragraph("• <b>David McClelland (Mid-20th Century):</b> Proposed that entrepreneurs are driven by a high 'Need for Achievement' (nAch). This includes a desire for personal responsibility, moderate risk-taking, and a need for feedback on performance.", bold_point_style))
    story.append(Paragraph("• <b>Julian Rotter (Mid-20th Century):</b> Introduced the concept of 'Locus of Control.' Entrepreneurs are often found to have a strong internal locus of control, believing they can influence events and their outcomes, rather than being at the mercy of external forces (external locus of control).", bold_point_style))
    story.append(Paragraph("• <b>Other Traits:</b> Research in this area has also explored traits like risk propensity, tolerance for ambiguity, innovativeness, proactiveness, and self-efficacy.", bold_point_style))

    story.append(Paragraph("3. The Sociological/Cultural School of Thought:", sub_heading_style))
    story.append(Paragraph("This perspective examines how societal and cultural factors influence the emergence and behavior of entrepreneurs.", body_style))
    story.append(Paragraph("• <b>Max Weber (Early 20th Century):</b> In 'The Protestant Ethic and the Spirit of Capitalism,' Weber suggested that certain religious beliefs (e.g., Calvinism) fostered values like hard work, thrift, and rationality, which were conducive to capitalist development and entrepreneurship.", bold_point_style))
    story.append(Paragraph("• <b>Everett Hagen (Mid-20th Century):</b> Argued that entrepreneurship often arises from groups experiencing 'withdrawal of status respect' or social marginalization, leading them to seek alternative paths to success and recognition.", bold_point_style))
    story.append(Paragraph("• <b>Thomas Cochran (Mid-20th Century):</b> Emphasized the role of cultural values, role expectations, and social sanctions in shaping entrepreneurial behavior. He suggested that entrepreneurship is more likely in societies that value and support it.", bold_point_style))
    story.append(Paragraph("• <b>Network Theory:</b> Modern sociological approaches also highlight the importance of social networks, relationships, and embeddedness in accessing resources, information, and support for entrepreneurial ventures.", bold_point_style))

    story.append(Paragraph("4. The Management/Behavioral School of Thought:", sub_heading_style))
    story.append(Paragraph("This school views entrepreneurship as a set of learnable skills and behaviors related to opportunity identification, resource acquisition, and venture management.", body_style))
    story.append(Paragraph("• <b>Peter Drucker (Late 20th Century):</b> A prominent management theorist, Drucker viewed entrepreneurship as a discipline that can be learned and practiced. He emphasized 'purposeful innovation' as the core of entrepreneurship and identified sources of innovative opportunity. He stressed that entrepreneurship is not about personality but about behavior.", bold_point_style))
    story.append(Paragraph("• <b>Focus on Process:</b> This school often breaks down entrepreneurship into a series of stages or activities, such as opportunity recognition, business planning, resource mobilization, launching, and managing growth. It looks at what entrepreneurs *do* rather than who they *are*.", bold_point_style))

    story.append(Paragraph("<u>Conclusion:</u>", sub_heading_style))
    story.append(Paragraph("The evolution of entrepreneurship thought reflects a growing understanding of its complexity. No single school provides a complete picture. Modern perspectives tend to be integrative, recognizing that entrepreneurship is influenced by economic conditions, individual psychological traits, socio-cultural contexts, and manageable behaviors. This holistic view is crucial for fostering entrepreneurship effectively in diverse settings.", body_style))

    story.append(Paragraph("Memory Trick: 'Every Person Should Manage' (Economic, Psychological, Sociological, Management) to remember the main schools of thought.", memory_trick_style))
    story.append(Paragraph("Diagram Suggestion: A timeline showing key thinkers under each school of thought and their approximate period of influence.", diagram_suggestion_style))

    story.append(Paragraph("Key Points to Expand Further:", expand_points_style))
    story.append(Paragraph("• Discuss the limitations of each school of thought (e.g., trait approach being too deterministic, economic models being too abstract).", body_style))
    story.append(Paragraph("• Explore the concept of 'Intrapreneurship' as a modern extension, particularly from the management school.", body_style))
    story.append(Paragraph("• Link the evolution to changing global economic landscapes (e.g., rise of tech entrepreneurship).", body_style))
    story.append(Spacer(1, 0.5*cm))


    # --- Question 2 ---
    story.append(Paragraph("2. What is Competence? Explain various types of Entrepreneurial Competencies.", question_style))

    story.append(Paragraph("<u>Definition of Competence:</u>", sub_heading_style))
    story.append(Paragraph("<b>Competence</b>, in a general sense, refers to the ability of an individual to perform a specific task or role successfully and efficiently. It is a cluster of related knowledge, skills, abilities, and attitudes (KSAs) that are observable, measurable, and critical to successful performance. Competence is not just about knowing *what* to do, but also knowing *how* to do it effectively and consistently in various situations.", body_style))
    story.append(Paragraph("In the context of entrepreneurship, competence means possessing and applying the necessary KSAs to identify opportunities, launch, manage, and grow a new venture despite uncertainties and challenges.", body_style))

    story.append(Paragraph("<u>Types of Entrepreneurial Competencies:</u>", sub_heading_style))
    story.append(Paragraph("Entrepreneurial competencies are specific sets of skills, knowledge, and attributes that enable entrepreneurs to perform their roles effectively. While various frameworks exist, some commonly recognized types include:", body_style))

    story.append(Paragraph("1. <b>Opportunity Competencies:</b>", bold_point_style))
    story.append(Paragraph("These relate to the entrepreneur's ability to perceive, create, evaluate, and exploit new business opportunities.", body_style))
    story.append(Paragraph("•   <i>Opportunity Recognition:</i> Identifying unmet needs, market gaps, or new applications for existing technologies.", bold_point_style))
    story.append(Paragraph("•   <i>Opportunity Assessment:</i> Evaluating the feasibility, viability, and potential risks/rewards of an identified opportunity.", bold_point_style))
    story.append(Paragraph("•   <i>Creativity and Innovation:</i> Developing novel solutions, products, services, or business models.", bold_point_style))

    story.append(Paragraph("2. <b>Relationship Competencies (Social Competencies):</b>", bold_point_style))
    story.append(Paragraph("These involve the skills needed to build and maintain positive and productive relationships with various stakeholders.", body_style))
    story.append(Paragraph("•   <i>Networking:</i> Building and leveraging a diverse network of contacts for information, resources, and support.", bold_point_style))
    story.append(Paragraph("•   <i>Leadership and Motivation:</i> Inspiring and guiding a team, delegating effectively, and fostering a positive work environment.", bold_point_style))
    story.append(Paragraph("•   <i>Communication Skills:</i> Articulating ideas clearly (written and verbal), active listening, and persuasive communication.", bold_point_style))
    story.append(Paragraph("•   <i>Negotiation and Conflict Resolution:</i> Achieving mutually beneficial agreements and managing disagreements constructively.", bold_point_style))

    story.append(Paragraph("3. <b>Conceptual Competencies (Cognitive Competencies):</b>", bold_point_style))
    story.append(Paragraph("These relate to the entrepreneur's mental abilities to understand complex situations, solve problems, and make effective decisions.", body_style))
    story.append(Paragraph("•   <i>Problem-Solving:</i> Identifying the root causes of problems and developing effective solutions.", bold_point_style))
    story.append(Paragraph("•   <i>Decision-Making:</i> Making timely and informed choices, often under conditions of uncertainty.", bold_point_style))
    story.append(Paragraph("•   <i>Analytical and Critical Thinking:</i> Evaluating information objectively and logically.", bold_point_style))
    story.append(Paragraph("•   <i>Learning Orientation:</i> A willingness to learn from experiences (both successes and failures) and adapt.", bold_point_style))

    story.append(Paragraph("4. <b>Organizing and Management Competencies:</b>", bold_point_style))
    story.append(Paragraph("These involve the skills required to plan, organize, and manage resources effectively to achieve business objectives.", body_style))
    story.append(Paragraph("•   <i>Planning and Goal Setting:</i> Defining clear objectives and developing strategies and action plans to achieve them (e.g., business planning).", bold_point_style))
    story.append(Paragraph("•   <i>Resource Mobilization and Management:</i> Acquiring and efficiently utilizing financial, human, and physical resources.", bold_point_style))
    story.append(Paragraph("•   <i>Financial Management:</i> Understanding financial statements, budgeting, managing cash flow, and making investment decisions.", bold_point_style))
    story.append(Paragraph("•   <i>Operational Management:</i> Managing day-to-day operations, ensuring quality, and optimizing processes.", bold_point_style))

    story.append(Paragraph("5. <b>Strategic Competencies:</b>", bold_point_style))
    story.append(Paragraph("These relate to the entrepreneur's ability to think long-term, define a vision, and position the venture for sustained competitive advantage.", body_style))
    story.append(Paragraph("•   <i>Visioning:</i> Creating a compelling and clear vision for the future of the venture.", bold_point_style))
    story.append(Paragraph("•   <i>Strategic Thinking and Formulation:</i> Analyzing the competitive landscape, identifying strategic options, and formulating effective strategies.", bold_point_style))
    story.append(Paragraph("•   <i>Adaptability and Flexibility:</i> Responding effectively to changes in the market or business environment.", bold_point_style))

    story.append(Paragraph("6. <b>Commitment Competencies (Personal/Self-Management Competencies):</b>", bold_point_style))
    story.append(Paragraph("These are personal attributes that drive the entrepreneur's actions and perseverance.", body_style))
    story.append(Paragraph("•   <i>Perseverance and Resilience:</i> Persisting in the face of obstacles, setbacks, and failures.", bold_point_style))
    story.append(Paragraph("•   <i>Initiative and Proactiveness:</i> Taking action without being told and anticipating future needs or problems.", bold_point_style))
    story.append(Paragraph("•   <i>Self-Confidence and Self-Efficacy:</i> Believing in one's own abilities to succeed.", bold_point_style))
    story.append(Paragraph("•   <i>Risk Propensity (Calculated):</i> Willingness to take calculated risks after assessing potential outcomes.", bold_point_style))
    story.append(Paragraph("•   <i>Passion and Dedication:</i> Deep commitment to the venture and its goals.", bold_point_style))

    story.append(Paragraph("<u>Conclusion:</u>", sub_heading_style))
    story.append(Paragraph("Entrepreneurial competencies are not innate; many can be learned and developed over time through education, experience, and mentorship. A successful entrepreneur typically possesses a blend of these competencies, and the relative importance of each may vary depending on the stage of the venture, the industry, and the specific context. Recognizing and cultivating these competencies is crucial for aspiring and existing entrepreneurs.", body_style))

    story.append(Paragraph("Memory Trick: 'ORC-OSC' for the competencies: Opportunity, Relationship, Conceptual, Organizing, Strategic, Commitment. (Imagine an ORC who is good at OSCillating between strategies and commitments!)", memory_trick_style))
    story.append(Paragraph("Diagram Suggestion: A circular or hub-and-spoke diagram with 'Entrepreneurial Success' at the center and the different competency categories radiating outwards, with specific skills listed under each.", diagram_suggestion_style))

    story.append(Paragraph("Key Points to Expand Further:", expand_points_style))
    story.append(Paragraph("• Discuss how these competencies can be assessed or measured.", body_style))
    story.append(Paragraph("• Provide examples of famous entrepreneurs and the specific competencies they demonstrated.", body_style))
    story.append(Paragraph("• Explain how entrepreneurial education and training programs aim to develop these competencies.", body_style))
    story.append(Spacer(1, 0.5*cm))


    # --- Question 3 ---
    story.append(Paragraph("3. What is a Group Entrepreneurship? Explain various types of Group Entrepreneurship.", question_style))

    story.append(Paragraph("<u>Definition of Group Entrepreneurship:</u>", sub_heading_style))
    story.append(Paragraph("<b>Group Entrepreneurship</b>, also known as team entrepreneurship or collective entrepreneurship, refers to entrepreneurial activities undertaken by two or more individuals who collectively pool their resources, skills, knowledge, and efforts to identify an opportunity, create, launch, and manage a new venture. Unlike solo entrepreneurship where a single individual drives the venture, group entrepreneurship emphasizes collaboration, shared decision-making, and distributed responsibilities among the founding members.", body_style))
    story.append(Paragraph("The core idea is that a team can often bring a wider range of competencies, greater financial capital, and more robust problem-solving capabilities than a single entrepreneur. It also allows for shared risk and workload.", body_style))

    story.append(Paragraph("<u>Various Types of Group Entrepreneurship:</u>", sub_heading_style))
    story.append(Paragraph("Group entrepreneurship can manifest in several forms, each with its own characteristics, legal structures, and operational dynamics:", body_style))

    story.append(Paragraph("1. <b>Founding Teams / Co-founderships:</b>", bold_point_style))
    story.append(Paragraph("This is the most common image of group entrepreneurship, where a small group of individuals (co-founders) come together with a shared vision to start a new company. They typically share equity and play active roles in the business. The success of such ventures often depends on the complementarity of skills, shared values, and effective communication among co-founders.", body_style))
    story.append(Paragraph("<i>Example:</i> Steve Jobs, Steve Wozniak, and Ronald Wayne co-founding Apple.", bold_point_style))

    story.append(Paragraph("2. <b>Family Businesses:</b>", bold_point_style))
    story.append(Paragraph("These are enterprises where ownership and/or management are controlled by members of the same family. Entrepreneurship within families can span generations. While they offer unique strengths like trust and long-term commitment, they can also face challenges related to succession planning, nepotism, and work-life balance.", body_style))
    story.append(Paragraph("<i>Example:</i> The Ford Motor Company, Reliance Industries (India).", bold_point_style))

    story.append(Paragraph("3. <b>Partnerships:</b>", bold_point_style))
    story.append(Paragraph("A formal legal structure where two or more individuals (partners) agree to share in the profits or losses of a business. A partnership agreement outlines the responsibilities, contributions, and profit/loss sharing ratios.", body_style))
    story.append(Paragraph("•   <i>General Partnership:</i> All partners share in the business's operational management and liability.", bold_point_style))
    story.append(Paragraph("•   <i>Limited Partnership:</i> Includes general partners (who manage and have unlimited liability) and limited partners (who invest capital but have limited liability and no management role).", bold_point_style))
    story.append(Paragraph("<i>Example:</i> Many law firms and accounting firms are structured as partnerships.", bold_point_style))

    story.append(Paragraph("4. <b>Cooperatives:</b>", bold_point_style))
    story.append(Paragraph("A cooperative is an autonomous association of persons united voluntarily to meet their common economic, social, and cultural needs and aspirations through a jointly-owned and democratically-controlled enterprise. Members are both owners and users.", body_style))
    story.append(Paragraph("Types include consumer cooperatives, producer cooperatives (e.g., agricultural co-ops like Amul), worker cooperatives, and housing cooperatives.", bold_point_style))
    story.append(Paragraph("<i>Example:</i> Amul (Anand Milk Union Limited) in India, Mondragon Corporation in Spain (a federation of worker cooperatives).", bold_point_style))

    story.append(Paragraph("5. <b>Joint Ventures (JVs):</b>", bold_point_style))
    story.append(Paragraph("A business arrangement where two or more independent companies agree to pool their resources to accomplish a specific task or project. This new entity is distinct from the parent companies. JVs are often formed to enter new markets, share R&D costs, or combine complementary technologies.", body_style))
    story.append(Paragraph("<i>Example:</i> Sony Ericsson (a JV between Sony and Ericsson for mobile phones, now defunct). Maruti Suzuki (initially a JV between Maruti Udyog Ltd of India and Suzuki of Japan).", bold_point_style))

    story.append(Paragraph("6. <b>Corporate Venturing / Intrapreneurship (Group-led):</b>", bold_point_style))
    story.append(Paragraph("While intrapreneurship can be individual, it often involves teams within an existing corporation acting entrepreneurially to develop new products, services, or business units. The corporation provides resources and a supportive environment. This is a form of internal group entrepreneurship.", body_style))
    story.append(Paragraph("<i>Example:</i> Google's '20% time' policy leading to Gmail, developed by a small team.", bold_point_style))

    story.append(Paragraph("7. <b>Franchising (from a multi-unit franchisee perspective):</b>", bold_point_style))
    story.append(Paragraph("While a single franchise unit might be run by an individual, a group of individuals might form a company to acquire and manage multiple franchise units. This collective entity acts entrepreneurially within the franchisor's framework.", body_style))
    story.append(Paragraph("<i>Example:</i> A group forming a company to operate several McDonald's outlets.", bold_point_style))

    story.append(Paragraph("<u>Conclusion:</u>", sub_heading_style))
    story.append(Paragraph("Group entrepreneurship offers significant advantages such as diverse skill sets, increased capital, shared risk, and enhanced decision-making. However, it also presents challenges like potential conflicts, slower decision-making if consensus is always required, and complexities in equity distribution. The success of group entrepreneurship heavily relies on clear roles, shared vision, trust, effective communication, and robust governance mechanisms. The choice of structure depends on the venture's goals, the relationship between members, and legal/tax considerations.", body_style))

    story.append(Paragraph("Memory Trick: 'Founding Families Partner Cooperatively in Joint Corporate Franchises.' (Founding Teams, Family Businesses, Partnerships, Cooperatives, Joint Ventures, Corporate Venturing, Franchises).", memory_trick_style))
    story.append(Paragraph("Diagram Suggestion: A mind map branching out from 'Group Entrepreneurship' to its various types, with brief characteristics for each type.", diagram_suggestion_style))

    story.append(Paragraph("Key Points to Expand Further:", expand_points_style))
    story.append(Paragraph("• Discuss the pros and cons of group entrepreneurship compared to solo entrepreneurship in more detail.", body_style))
    story.append(Paragraph("• Elaborate on the critical success factors for founding teams (e.g., team composition, conflict resolution mechanisms).", body_style))
    story.append(Paragraph("• Explore the legal implications and differences in liability for different types of group structures.", body_style))
    story.append(Spacer(1, 0.5*cm))


    # --- Question 4 ---
    story.append(Paragraph("4. Explain the concept behind formation of Micro, Small and Medium Enterprises (MSMEs). Describe its characteristics and relevance.", question_style))

    story.append(Paragraph("<u>Concept Behind Formation of MSMEs:</u>", sub_heading_style))
    story.append(Paragraph("The concept behind the formation and promotion of Micro, Small, and Medium Enterprises (MSMEs) stems from their widely recognized potential to drive socio-economic development. Governments and policymakers worldwide support MSMEs due to their unique contributions that larger corporations often cannot replicate with the same efficiency or societal impact. The core ideas are:", body_style))
    story.append(Paragraph("• <b>Employment Generation:</b> MSMEs are typically more labor-intensive than large corporations, making them crucial for creating jobs, especially in developing economies and rural areas. Jargon: 'Labor-intensive' – requiring a large amount of labor relative to capital.", bold_point_style))
    story.append(Paragraph("• <b>Equitable Distribution of Income and Wealth:</b> By fostering entrepreneurship at grassroots levels, MSMEs help in dispersing economic power and reducing income disparities, preventing wealth concentration in a few hands.", bold_point_style))
    story.append(Paragraph("• <b>Mobilization of Local Resources:</b> MSMEs often utilize local capital, skills, and raw materials, which might otherwise remain untapped, leading to value addition within the community.", bold_point_style))
    story.append(Paragraph("• <b>Promotion of Innovation and Entrepreneurship:</b> They serve as a breeding ground for new ideas, innovations, and entrepreneurial talent. Many large corporations started as small enterprises.", bold_point_style))
    story.append(Paragraph("• <b>Balanced Regional Development:</b> MSMEs can be established in smaller towns and rural areas, helping to curb rural-urban migration and promote industrialization beyond major urban centers.", bold_point_style))
    story.append(Paragraph("• <b>Flexibility and Adaptability:</b> Smaller enterprises can often adapt more quickly to changing market conditions and customer needs compared to larger, more bureaucratic organizations.", bold_point_style))
    story.append(Paragraph("• <b>Contribution to Exports and GDP:</b> Collectively, MSMEs make significant contributions to a nation's Gross Domestic Product (GDP) and export earnings.", bold_point_style))
    story.append(Paragraph("• <b>Support to Large Industries (Ancillarization):</b> MSMEs often act as ancillary units, supplying components, sub-assemblies, and services to large-scale industries, thus forming an integral part of the industrial ecosystem.", bold_point_style))
    story.append(Paragraph("The definition of MSMEs usually varies by country and is typically based on criteria such as investment in plant and machinery/equipment, annual turnover, or number of employees. For example, in India, the MSMED Act, 2006 (and subsequent amendments) defines them based on investment and turnover criteria.", body_style))

    story.append(Paragraph("<u>Characteristics of MSMEs:</u>", sub_heading_style))
    story.append(Paragraph("MSMEs exhibit several common characteristics:", body_style))
    story.append(Paragraph("• <b>Low Capital Requirement:</b> Generally, they require less capital to start and operate compared to large enterprises.", bold_point_style))
    story.append(Paragraph("• <b>Localized Operations:</b> Many MSMEs cater to local or regional markets, though some also export.", bold_point_style))
    story.append(Paragraph("• <b>Owner-Managed:</b> Often, the owner is also the manager, leading to quick decision-making but also potential limitations in professional management expertise.", bold_point_style))
    story.append(Paragraph("• <b>High Labor Intensity:</b> They tend to use more labor per unit of output compared to capital.", bold_point_style))
    story.append(Paragraph("• <b>Flexibility:</b> Capable of adapting their production and operations to meet specific customer orders or changing market demands relatively quickly.", bold_point_style))
    story.append(Paragraph("• <b>Use of Indigenous Technology:</b> Many MSMEs rely on locally developed or adapted technologies.", bold_point_style))
    story.append(Paragraph("• <b>Closer Customer Relationships:</b> Due to their scale and often localized nature, they can maintain more personal relationships with customers.", bold_point_style))
    story.append(Paragraph("• <b>Informal Sector Linkages:</b> Many MSMEs, especially micro and some small enterprises, operate in or have strong links with the informal sector.", bold_point_style))
    story.append(Paragraph("• <b>Vulnerability:</b> They can be more vulnerable to economic downturns, competition from larger players, and changes in government policies.", bold_point_style))

    story.append(Paragraph("<u>Relevance of MSMEs:</u>", sub_heading_style))
    story.append(Paragraph("The relevance of MSMEs to an economy, particularly for developing countries like India, is immense:", body_style))
    story.append(Paragraph("• <b>Engine of Economic Growth:</b> They contribute significantly to GDP, industrial output, and value addition.", bold_point_style))
    story.append(Paragraph("• <b>Major Employment Provider:</b> After agriculture, the MSME sector is often the largest employer, absorbing a vast workforce, including skilled, semi-skilled, and unskilled labor.", bold_point_style))
    story.append(Paragraph("• <b>Fostering Inclusive Growth:</b> By providing opportunities to a wide cross-section of society, including women, minorities, and people in disadvantaged regions, MSMEs promote inclusive development.", bold_point_style))
    story.append(Paragraph("• <b>Innovation Hubs:</b> They are often sources of grassroots innovation and can be pioneers in niche markets.", bold_point_style))
    story.append(Paragraph("• <b>Export Promotion:</b> MSMEs contribute substantially to export earnings, often specializing in products like handicrafts, textiles, and light engineering goods.", bold_point_style))
    story.append(Paragraph("• <b>Development of Entrepreneurial Spirit:</b> They nurture a culture of entrepreneurship and self-reliance.", bold_point_style))
    story.append(Paragraph("• <b>Strengthening Industrial Base:</b> Through ancillarization and by creating a competitive environment, they strengthen the overall industrial structure of a country.", bold_point_style))
    story.append(Paragraph("• <b>Poverty Alleviation:</b> By creating livelihoods, MSMEs play a vital role in reducing poverty.", bold_point_style))

    story.append(Paragraph("<u>Conclusion:</u>", sub_heading_style))
    story.append(Paragraph("MSMEs are the backbone of most economies worldwide. Their formation is driven by the need for widespread economic participation, job creation, and balanced development. Despite facing challenges like access to finance, technology, and markets, their characteristics make them uniquely positioned to contribute to economic dynamism and social equity. Recognizing their relevance, governments implement various policies and support programs to nurture their growth and sustainability.", body_style))

    story.append(Paragraph("Memory Trick (Relevance): 'Jobs In Every Region Develop Nations' (Job creation, Inclusive growth, Export, Regional development, GDP contribution, Nurturing entrepreneurship).", memory_trick_style))
    story.append(Paragraph("Diagram Suggestion: A pyramid with MSMEs forming the broad base, supporting larger industries and the overall economy at the top. Or, a circular flow diagram showing MSMEs' contributions to households (jobs, income) and other businesses (supplies).", diagram_suggestion_style))

    story.append(Paragraph("Key Points to Expand Further:", expand_points_style))
    story.append(Paragraph("• Provide specific data/statistics on MSME contribution to GDP and employment in a particular country (e.g., India).", body_style))
    story.append(Paragraph("• Discuss common challenges faced by MSMEs (finance, technology, marketing, infrastructure, skilled labor).", body_style))
    story.append(Paragraph("• Outline some government policies or schemes aimed at supporting MSMEs.", body_style))
    story.append(Spacer(1, 0.5*cm))


    # --- Question 5 ---
    story.append(Paragraph("5. What are the sources of finance in business enterprise? Discuss.", question_style))

    story.append(Paragraph("<u>Introduction:</u>", sub_heading_style))
    story.append(Paragraph("Finance is the lifeblood of any business enterprise, essential for its establishment, operations, growth, and expansion. Access to adequate and timely finance is a critical determinant of entrepreneurial success. Business finance can be broadly categorized based on the period (short, medium, long-term), ownership (equity, debt), and source (internal, external).", body_style))
    story.append(Paragraph("Jargon: 'Equity finance' – funds raised by selling ownership stakes in the company. 'Debt finance' – funds borrowed that must be repaid with interest.", body_style))

    story.append(Paragraph("<u>Sources of Finance in Business Enterprise:</u>", sub_heading_style))
    story.append(Paragraph("The various sources of finance available to a business enterprise can be discussed as follows:", body_style))

    story.append(Paragraph("A. <b>Internal Sources (Generated within the business):</b>", bold_point_style))
    story.append(Paragraph("1. <b>Personal Savings / Owner's Capital (Bootstrapping):</b> Especially for startups and small businesses, the entrepreneur's own savings are often the primary initial source. This is also known as bootstrapping – funding the venture with personal finances or operating revenues.", bold_point_style))
    story.append(Paragraph("2. <b>Retained Earnings (Ploughing back of profits):</b> Profitable existing businesses can reinvest a portion of their net profits back into the company for growth and expansion, rather than distributing it all as dividends. This is a very important source of long-term finance for established companies.", bold_point_style))
    story.append(Paragraph("3. <b>Sale of Assets:</b> A business might sell off surplus or underutilized assets (e.g., old machinery, unused land) to generate funds.", bold_point_style))

    story.append(Paragraph("B. <b>External Sources (Raised from outside the business):</b>", bold_point_style))
    story.append(Paragraph("<u>I. Equity Finance (Ownership Capital):</u>", sub_heading_style))
    story.append(Paragraph("4. <b>Friends and Family:</b> Entrepreneurs often turn to close relations for initial capital, usually in exchange for equity or as an informal loan. While accessible, it can strain personal relationships if the venture fails.", bold_point_style))
    story.append(Paragraph("5. <b>Angel Investors:</b> Wealthy individuals who provide capital for business start-ups, usually in exchange for convertible debt or ownership equity. They often bring industry expertise and networks.", bold_point_style))
    story.append(Paragraph("6. <b>Venture Capital (VC) Firms:</b> Professional firms that invest in early-stage, high-potential, and often high-risk, growth companies. VCs invest in exchange for equity and typically seek a significant return on investment, often through an exit strategy like an IPO or acquisition. They usually take an active role in guiding the company.", bold_point_style))
    story.append(Paragraph("7. <b>Private Equity (PE) Firms:</b> Similar to VCs but usually invest in more mature companies, often for buyouts, restructuring, or expansion. They also take equity stakes.", bold_point_style))
    story.append(Paragraph("8. <b>Initial Public Offering (IPO) / Stock Market:</b> A company can raise substantial capital by selling shares to the public for the first time and getting listed on a stock exchange. This is typically for well-established, larger companies seeking significant expansion capital.", bold_point_style))
    story.append(Paragraph("9. <b>Crowdfunding (Equity-based):</b> Raising small amounts of money from a large number of people, typically via the internet, in exchange for equity in the company.", bold_point_style))

    story.append(Paragraph("<u>II. Debt Finance (Borrowed Capital):</u>", sub_heading_style))
    story.append(Paragraph("10. <b>Bank Loans (Term Loans and Working Capital Loans):</b> Commercial banks provide various types of loans. Term loans are for long-term investments (e.g., machinery, buildings), while working capital loans (e.g., overdrafts, cash credit) finance day-to-day operations. Collateral is often required.", bold_point_style))
    story.append(Paragraph("11. <b>Non-Banking Financial Companies (NBFCs):</b> These institutions also provide loans and financial services, sometimes with more flexible terms than banks but potentially higher interest rates.", bold_point_style))
    story.append(Paragraph("12. <b>Debentures / Bonds:</b> Companies can issue debentures (unsecured) or bonds (often secured) to the public or institutions, which are debt instruments with a fixed interest rate and maturity date.", bold_point_style))
    story.append(Paragraph("13. <b>Trade Credit:</b> Suppliers may allow businesses to purchase goods or services on credit, effectively providing short-term finance. This is a common source for managing working capital.", bold_point_style))
    story.append(Paragraph("14. <b>Leasing and Hire Purchase:</b>", bold_point_style))
    story.append(Paragraph("   •   <i>Leasing:</i> Acquiring the use of an asset (e.g., equipment, vehicles) by paying regular lease rentals for a specified period, without owning it. This avoids large upfront capital expenditure.", bold_point_style))
    story.append(Paragraph("   •   <i>Hire Purchase:</i> Acquiring an asset by paying installments over a period. Ownership transfers to the hirer after the last installment is paid.", bold_point_style))
    story.append(Paragraph("15. <b>Government Schemes and Subsidies:</b> Many governments offer financial assistance, grants, or subsidized loans to promote specific sectors (e.g., MSMEs, startups, green technology).", bold_point_style))
    story.append(Paragraph("16. <b>Crowdfunding (Debt-based / Peer-to-Peer Lending):</b> Raising loans from multiple individuals online, with an agreement to repay with interest.", bold_point_style))
    story.append(Paragraph("17. <b>Factoring and Forfaiting:</b>", bold_point_style))
    story.append(Paragraph("   •   <i>Factoring:</i> Selling accounts receivable (invoices) to a third party (a factor) at a discount to get immediate cash.", bold_point_style))
    story.append(Paragraph("   •   <i>Forfaiting:</i> Similar to factoring but usually for international trade receivables, longer-term, and without recourse to the exporter.", bold_point_style))

    story.append(Paragraph("<u>Discussion and Considerations:</u>", sub_heading_style))
    story.append(Paragraph("Choosing the right source of finance depends on various factors:", body_style))
    story.append(Paragraph("• <b>Purpose and Period:</b> Long-term assets are best financed by long-term sources; working capital by short-term sources.", bold_point_style))
    story.append(Paragraph("• <b>Cost:</b> Interest rates for debt, dilution of ownership for equity.", bold_point_style))
    story.append(Paragraph("• <b>Risk:</b> Debt increases financial risk due to fixed repayment obligations. Equity is less risky for the firm but dilutes control.", bold_point_style))
    story.append(Paragraph("• <b>Control:</b> Equity financing can dilute the original owners' control, while debt financing generally does not (unless covenants are breached).", bold_point_style))
    story.append(Paragraph("• <b>Flexibility:</b> Some sources come with restrictive covenants or conditions.", bold_point_style))
    story.append(Paragraph("• <b>Availability and Eligibility:</b> Not all sources are available to all types or sizes of businesses (e.g., IPOs are for larger companies).", bold_point_style))
    story.append(Paragraph("A balanced capital structure, often a mix of debt and equity, is usually optimal.", body_style))

    story.append(Paragraph("<u>Conclusion:</u>", sub_heading_style))
    story.append(Paragraph("A wide array of financing sources is available to business enterprises, each with its own merits, demerits, and suitability. Entrepreneurs must carefully evaluate their financial needs, the stage of their business, and the characteristics of each source to make informed financing decisions that support the venture's viability and growth.", body_style))

    story.append(Paragraph("Memory Trick: Think of finance sources like layers of an 'Onion': 'Owner's Core', then 'Friends/Family Ring', then 'Angel/VC Layer', then 'Bank/Market Skin'. (This helps visualize progression but isn't exhaustive). Or, 'DEBT' vs 'EQUITY' as main branches.", memory_trick_style))
    story.append(Paragraph("Diagram Suggestion: A tree diagram categorizing sources into Internal/External, and then further into Equity/Debt and Short/Long-term.", diagram_suggestion_style))

    story.append(Paragraph("Key Points to Expand Further:", expand_points_style))
    story.append(Paragraph("• Discuss the concept of 'capital structure' and its importance.", body_style))
    story.append(Paragraph("• Elaborate on the challenges faced by startups in accessing finance.", body_style))
    story.append(Paragraph("• Compare and contrast debt financing vs. equity financing in more detail, including tax implications.", body_style))
    story.append(Spacer(1, 0.5*cm))


    # --- Question 6 ---
    story.append(Paragraph("6. What are the factors which determine the location decisions of an enterprise? Discuss.", question_style))

    story.append(Paragraph("<u>Introduction:</u>", sub_heading_style))
    story.append(Paragraph("The location decision for an enterprise is a critical strategic choice that can significantly impact its operational efficiency, cost structure, market access, and long-term profitability. It's a long-term commitment and often involves substantial investment, making it difficult and costly to reverse. Therefore, businesses undertake careful analysis of various factors before selecting an optimal location.", body_style))
    story.append(Paragraph("Jargon: 'Optimal location' – a site that minimizes costs and maximizes benefits for the enterprise.", body_style))

    story.append(Paragraph("<u>Factors Determining Location Decisions:</u>", sub_heading_style))
    story.append(Paragraph("The factors influencing location decisions can be broadly categorized, though they often interrelate:", body_style))

    story.append(Paragraph("1. <b>Proximity to Market:</b>", bold_point_style))
    story.append(Paragraph("•   For businesses producing perishable goods, or those where transportation costs of finished products are high (e.g., bulky items), or where quick customer service is crucial (e.g., retail, services), being close to the target market is vital.", bold_point_style))
    story.append(Paragraph("•   Reduces distribution costs and delivery times, enhances customer responsiveness.", bold_point_style))

    story.append(Paragraph("2. <b>Availability and Proximity of Raw Materials:</b>", bold_point_style))
    story.append(Paragraph("•   Industries that process bulky or perishable raw materials, or where raw material transportation costs are high, often locate near the source of these materials (e.g., sugar mills near sugarcane fields, paper mills near forests).", bold_point_style))
    story.append(Paragraph("•   Ensures a steady and cost-effective supply of inputs.", bold_point_style))

    story.append(Paragraph("3. <b>Availability of Labor:</b>", bold_point_style))
    story.append(Paragraph("•   Access to a pool of skilled, semi-skilled, or unskilled labor at reasonable wage rates is crucial. The specific labor requirements depend on the nature of the industry.", bold_point_style))
    story.append(Paragraph("•   Labor productivity, industrial relations climate (e.g., unionization levels, history of strikes), and availability of specialized skills are key considerations.", bold_point_style))

    story.append(Paragraph("4. <b>Infrastructure Facilities:</b>", bold_point_style))
    story.append(Paragraph("•   <b>Transportation:</b> Availability of roads, railways, ports, and airports for movement of raw materials and finished goods.", bold_point_style))
    story.append(Paragraph("•   <b>Power:</b> Reliable and adequate supply of electricity at competitive rates.", bold_point_style))
    story.append(Paragraph("•   <b>Water:</b> Sufficient supply of water, especially for process industries.", bold_point_style))
    story.append(Paragraph("•   <b>Communication:</b> Good telecommunication and internet connectivity.", bold_point_style))
    story.append(Paragraph("•   <b>Waste Disposal:</b> Facilities for safe and compliant disposal of industrial waste.", bold_point_style))

    story.append(Paragraph("5. <b>Government Policies and Regulations:</b>", bold_point_style))
    story.append(Paragraph("•   Government incentives such as tax holidays, subsidies, grants, and development of Special Economic Zones (SEZs) or industrial parks can attract businesses.", bold_point_style))
    story.append(Paragraph("•   Conversely, stringent regulations, high taxes, or political instability can deter investment.", bold_point_style))
    story.append(Paragraph("•   Local zoning laws, environmental regulations, and licensing procedures also play a role.", bold_point_style))

    story.append(Paragraph("6. <b>Cost of Land and Construction:</b>", bold_point_style))
    story.append(Paragraph("•   The price of land, availability of suitable sites, and the cost of constructing facilities vary significantly between locations. This is a major upfront investment.", bold_point_style))

    story.append(Paragraph("7. <b>Industrial Climate and Agglomeration Economies:</b>", bold_point_style))
    story.append(Paragraph("•   <b>Agglomeration Economies:</b> Benefits that firms obtain by locating near each other ('clustering'). This can include access to a specialized labor pool, supplier networks, shared infrastructure, and knowledge spillovers (e.g., Silicon Valley for tech, Detroit for auto historically).", bold_point_style))
    story.append(Paragraph("•   Presence of supporting industries (ancillary units, repair services) and a favorable business environment.", bold_point_style))

    story.append(Paragraph("8. <b>Environmental Factors and Regulations:</b>", bold_point_style))
    story.append(Paragraph("•   Climatic conditions suitable for the industry or employees.", bold_point_style))
    story.append(Paragraph("•   Increasingly important are environmental impact assessments and regulations related to pollution control and sustainability. Some locations may be off-limits for certain types of industries.", bold_point_style))

    story.append(Paragraph("9. <b>Access to Finance and Support Services:</b>", bold_point_style))
    story.append(Paragraph("•   Availability of banks, financial institutions, and other support services like legal, accounting, and consulting firms.", bold_point_style))

    story.append(Paragraph("10. <b>Personal Factors (especially for Small Businesses):</b>", bold_point_style))
    story.append(Paragraph("•   For small entrepreneurs, personal preferences, family ties, or proximity to home can significantly influence the location choice, sometimes overriding purely economic factors.", bold_point_style))

    story.append(Paragraph("11. <b>Political Stability and Security:</b>", bold_point_style))
    story.append(Paragraph("•   A stable political environment, rule of law, and security of assets and personnel are fundamental for long-term business operations.", bold_point_style))

    story.append(Paragraph("12. <b>Global and International Factors (for MNCs):</b>", bold_point_style))
    story.append(Paragraph("•   For multinational corporations, factors like exchange rates, trade barriers, host country regulations, cultural differences, and access to international markets become critical.", bold_point_style))

    story.append(Paragraph("<u>Discussion:</u>", sub_heading_style))
    story.append(Paragraph("The relative importance of these factors varies depending on the type of industry (manufacturing, service, retail), scale of operations, and specific business strategy. For instance, a software development company might prioritize skilled labor and communication infrastructure, while a heavy manufacturing plant might focus on raw materials, power, and transport. Businesses often use quantitative methods (e.g., factor rating, break-even analysis) and qualitative judgment to evaluate potential locations.", body_style))
    story.append(Paragraph("The decision is often a trade-off. No single location may be perfect on all counts, so the enterprise must weigh the factors according to its priorities to find the most advantageous or 'optimal' location.", body_style))

    story.append(Paragraph("<u>Conclusion:</u>", sub_heading_style))
    story.append(Paragraph("Selecting the right location is a complex, multi-faceted decision that requires thorough research and careful consideration of numerous inter-dependent factors. A well-chosen location can provide a competitive edge and contribute to the success and sustainability of the enterprise, while a poor choice can lead to operational inefficiencies and financial strain.", body_style))

    story.append(Paragraph("Memory Trick: 'Market & Materials Labor Infrastructure, Government Costs Industry, Environment & Personal Politics' (MMLI GC IEPP - a bit clunky, but covers key areas). Or, think of building a house: 'Location, Location, Location' and what makes a good one (access, resources, community, safety).", memory_trick_style))
    story.append(Paragraph("Diagram Suggestion: A mind map with 'Location Decision' at the center, branching out to these key factors. Each branch can have sub-points or examples.", diagram_suggestion_style))

    story.append(Paragraph("Key Points to Expand Further:", expand_points_style))
    story.append(Paragraph("• Discuss specific location models or techniques used in decision-making (e.g., Center of Gravity method, Factor Rating method).", body_style))
    story.append(Paragraph("• Provide examples of companies that made successful or unsuccessful location decisions and the reasons why.", body_style))
    story.append(Paragraph("• Discuss the impact of globalization and technology (e.g., remote work) on location decisions.", body_style))
    story.append(Spacer(1, 0.5*cm))


    # --- Question 7 ---
    story.append(Paragraph("7. What is Social Entrepreneurship? Explain the four major elements of social entrepreneurship.", question_style))

    story.append(Paragraph("<u>Definition of Social Entrepreneurship:</u>", sub_heading_style))
    story.append(Paragraph("<b>Social Entrepreneurship</b> is an approach by individuals, groups, start-up companies or entrepreneurs, in which they develop, fund and implement solutions to social, cultural, or environmental issues. It combines the passion of a social mission with the discipline, innovation, and determination traditionally associated with business entrepreneurship. Unlike traditional entrepreneurs who are primarily driven by profit, social entrepreneurs are primarily driven by a desire to create positive social impact or systemic change. However, this does not mean they ignore financial sustainability; many social enterprises aim to be financially self-sufficient or even profitable, with profits often reinvested into the social mission.", body_style))
    story.append(Paragraph("Jargon: 'Social Mission' – The primary goal of addressing a specific social or environmental problem. 'Systemic Change' – Fundamental change in policies, practices, or social structures to resolve underlying causes of problems.", body_style))
    story.append(Paragraph("Key figures like J. Gregory Dees have significantly contributed to defining and popularizing the concept. The core is applying entrepreneurial thinking to solve social problems.", body_style))

    story.append(Paragraph("<u>The Four Major Elements of Social Entrepreneurship:</u>", sub_heading_style))
    story.append(Paragraph("While various scholars and practitioners might emphasize different aspects, a widely accepted framework, largely influenced by J. Gregory Dees, highlights several core elements. Often, these are distilled into key characteristics. Four frequently cited major elements are:", body_style))

    story.append(Paragraph("1. <b>Social Mission Primacy (Adopting a mission to create and sustain social value):</b>", bold_point_style))
    story.append(Paragraph("•   This is the cornerstone of social entrepreneurship. The primary objective is to generate social value or address a pressing social/environmental need, rather than personal wealth creation. This mission is explicit, central, and drives all strategic decisions.", bold_point_style))
    story.append(Paragraph("•   While economic value (profit) may be pursued, it is a means to an end (achieving the social mission) rather than the end itself. The social impact is the ultimate measure of success.", bold_point_style))
    story.append(Paragraph("•   <i>Example:</i> Grameen Bank's mission to provide microcredit to impoverished women to alleviate poverty.", bold_point_style))

    story.append(Paragraph("2. <b>Innovation (Recognizing and relentlessly pursuing new opportunities to serve that mission):</b>", bold_point_style))
    story.append(Paragraph("•   Social entrepreneurs are not content with traditional approaches if they are ineffective. They actively seek out and apply innovative solutions to social problems. This can involve new products, services, delivery models, organizational structures, or resource mobilization strategies.", bold_point_style))
    story.append(Paragraph("•   This echoes Schumpeter's concept of the entrepreneur as an innovator, but applied to the social sector. It involves creativity, resourcefulness, and a willingness to challenge existing norms.", bold_point_style))
    story.append(Paragraph("•   <i>Example:</i> Aravind Eye Care System's innovative high-volume, low-cost model for cataract surgeries to combat blindness.", bold_point_style))

    story.append(Paragraph("3. <b>Adaptability and Continuous Learning (Engaging in a process of continuous innovation, adaptation, and learning):</b>", bold_point_style))
    story.append(Paragraph("•   The environments in which social entrepreneurs operate are often complex and dynamic. Therefore, they must be adaptable, learning from their experiences and the feedback from the communities they serve.", bold_point_style))
    story.append(Paragraph("•   This involves being responsive to changing needs, iterating on solutions, and being willing to modify or even abandon approaches that are not working. It's about being evidence-driven and outcome-focused.", bold_point_style))
    story.append(Paragraph("•   <i>Example:</i> Many social enterprises pivot their models based on field results and community feedback to better achieve their impact goals.", bold_point_style))
    story.append(Paragraph("   (Note: Some frameworks might combine this with innovation or emphasize 'Scalability and Sustainability' as a distinct element for broader impact.)", body_style))


    story.append(Paragraph("4. <b>Entrepreneurial Acumen and Accountability (Exhibiting a heightened sense of accountability to the constituencies served and for the outcomes created):</b>", bold_point_style))
    story.append(Paragraph("•   Social entrepreneurs apply business-like discipline, determination, and resourcefulness to achieve their social goals. They are not just well-intentioned; they are also effective managers and leaders.", bold_point_style))
    story.append(Paragraph("•   Crucially, they hold themselves accountable for the social impact they create. This involves measuring and reporting on their social performance, not just financial performance, to stakeholders (beneficiaries, funders, staff, public).", bold_point_style))
    story.append(Paragraph("•   This element emphasizes action-orientation, boldness in the face of challenges, and a commitment to producing tangible, positive results.", bold_point_style))
    story.append(Paragraph("•   <i>Example:</i> Social enterprises using impact metrics like SROI (Social Return on Investment) to demonstrate their value.", bold_point_style))

    story.append(Paragraph("Alternative Element Often Highlighted - **Scalability and Sustainability**:", sub_heading_style))
    story.append(Paragraph("Many frameworks emphasize the drive to create scalable solutions that can be replicated or expanded to reach a larger population and achieve broader systemic change. Sustainability refers to the ability of the social venture to continue its operations and impact over the long term, often through diverse funding models that may include earned income.", body_style))


    story.append(Paragraph("<u>Conclusion:</u>", sub_heading_style))
    story.append(Paragraph("Social entrepreneurship represents a powerful force for positive change in the world. By combining a deep commitment to a social mission with entrepreneurial innovation, adaptability, and accountability, social entrepreneurs tackle some of society's most intractable problems. These core elements distinguish them from traditional businesses and purely charitable organizations, carving out a unique space where purpose and pragmatism intersect to create lasting social value.", body_style))

    story.append(Paragraph("Memory Trick for Dees-inspired elements: 'Social Mission Innovates, Adapts, and is Accountable' (SMIAA). Or, use 'SPIA' if considering 'Scalability/Sustainability' as a key element over 'Adaptability': Social Mission, Pursuit of Opportunity (Innovation), Impact (Accountability), Adaptability/Action-Orientation.", memory_trick_style))
    story.append(Paragraph("Diagram Suggestion: A Venn diagram showing the intersection of 'Social Mission,' 'Business Acumen,' and 'Innovation' to define Social Entrepreneurship. Or, a pillar diagram with the four elements supporting 'Social Impact'.", diagram_suggestion_style))

    story.append(Paragraph("Key Points to Expand Further:", expand_points_style))
    story.append(Paragraph("• Provide more detailed examples of well-known social entrepreneurs or enterprises (e.g., Muhammad Yunus, Blake Mycoskie of TOMS Shoes, Wendy Kopp of Teach For America).", body_style))
    story.append(Paragraph("• Discuss the spectrum of social enterprises (non-profit with earned income, for-profit with social mission, hybrid models).", body_style))
    story.append(Paragraph("• Explore the challenges faced by social entrepreneurs (e.g., funding, measuring social impact, scaling).", body_style))
    story.append(Spacer(1, 0.5*cm))

    # --- Question 8 ---
    story.append(Paragraph("8. Explain the major theories which revolve around ethics and determine ethical behaviour.", question_style))

    story.append(Paragraph("<u>Introduction:</u>", sub_heading_style))
    story.append(Paragraph("Ethics is the branch of philosophy that involves systematizing, defending, and recommending concepts of right and wrong conduct. Ethical theories provide frameworks for determining what constitutes ethical behavior and guiding moral decision-making in various situations, including business. Understanding these theories helps individuals and organizations navigate complex ethical dilemmas and foster a culture of integrity.", body_style))
    story.append(Paragraph("Jargon: 'Ethical Dilemma' – A situation where one must choose between two or more morally conflicting courses of action.", body_style))

    story.append(Paragraph("<u>Major Ethical Theories Determining Ethical Behaviour:</u>", sub_heading_style))
    story.append(Paragraph("Several major ethical theories have been developed over centuries, each offering a different perspective on how to determine ethical behavior. They can be broadly categorized into consequentialist (outcome-based) and non-consequentialist (duty-based or rights-based), along with character-based theories.", body_style))

    story.append(Paragraph("1. <b>Consequentialist Theories (Teleological Ethics):</b>", bold_point_style))
    story.append(Paragraph("These theories argue that the morality of an action is determined by its consequences or outcomes. An action is right if it produces good consequences and wrong if it produces bad consequences.", body_style))
    story.append(Paragraph("•   <b>Utilitarianism (Jeremy Bentham, John Stuart Mill):</b> The most prominent consequentialist theory. It states that an action is ethical if it produces the 'greatest good for the greatest number' of people. Decisions are made by weighing the potential benefits and harms to all affected parties and choosing the option that maximizes overall happiness or utility. Jargon: 'Utility' – often defined as happiness, pleasure, or well-being.", bold_point_style))
    story.append(Paragraph("    <i>Types of Utilitarianism:</i>", bold_point_style))
    story.append(Paragraph("    - <i>Act Utilitarianism:</i> Assesses each act individually for its utility.", bold_point_style))
    story.append(Paragraph("    - <i>Rule Utilitarianism:</i> Suggests following moral rules that, if generally followed, would produce the greatest good.", bold_point_style))
    story.append(Paragraph("    <i>Critiques:</i> Can be difficult to measure and compare utility for different people; may justify actions that harm minorities if they benefit the majority; ignores intentions and rights.", bold_point_style))
    story.append(Paragraph("•   <b>Ethical Egoism:</b> Argues that an action is moral if it promotes the individual's own long-term self-interest. This is distinct from selfishness, as long-term interests might involve cooperation or short-term sacrifices.", bold_point_style))

    story.append(Paragraph("2. <b>Non-Consequentialist Theories (Deontological Ethics):</b>", bold_point_style))
    story.append(Paragraph("These theories assert that the morality of an action is based on adherence to duties, rules, or obligations, regardless of the consequences.", body_style))
    story.append(Paragraph("•   <b>Kantian Ethics / Duty-Based Ethics (Immanuel Kant):</b> Emphasizes moral duties and universal principles. Kant proposed the 'Categorical Imperative' as the supreme principle of morality.", bold_point_style))
    story.append(Paragraph("    <i>Formulations of the Categorical Imperative:</i>", bold_point_style))
    story.append(Paragraph("    1. <i>Universality:</i> 'Act only according to that maxim whereby you can at the same time will that it should become a universal law.' (Could everyone act this way without contradiction?).", bold_point_style))
    story.append(Paragraph("    2. <i>Humanity as an End:</i> 'Act in such a way that you treat humanity, whether in your own person or in the person of any other, never merely as a means to an end, but always at the same time as an end.' (Respect for persons).", bold_point_style))
    story.append(Paragraph("    <i>Critiques:</i> Can be rigid and doesn't easily resolve conflicts between duties; consequences, though ignored, often seem relevant.", bold_point_style))
    story.append(Paragraph("•   <b>Rights Theory (John Locke, Thomas Jefferson):</b> Focuses on fundamental human rights that should be respected and protected. Actions are ethical if they uphold these rights (e.g., right to life, liberty, property, fair treatment). Rights can be positive (entitlements, e.g., right to education) or negative (protections from interference, e.g., right to free speech).", bold_point_style))
    story.append(Paragraph("    <i>Critiques:</i> Difficult to determine which rights are fundamental and how to resolve conflicting rights.", bold_point_style))

    story.append(Paragraph("3. <b>Virtue Ethics (Aristotle, Plato):</b>", bold_point_style))
    story.append(Paragraph("This theory focuses on the moral character of the person performing the action, rather than on duties or consequences. It asks 'What kind of person should I be?' and emphasizes cultivating virtues like honesty, compassion, courage, justice, and temperance. An action is ethical if it is what a virtuous person would do in the circumstances.", body_style))
    story.append(Paragraph("•   It emphasizes moral education and development of good character traits (virtues) and avoidance of vices.", bold_point_style))
    story.append(Paragraph("•   Aristotle's concept of the 'Golden Mean' suggests that virtue often lies between two extremes (e.g., courage is the mean between cowardice and recklessness).", bold_point_style))
    story.append(Paragraph("•   <i>Critiques:</i> Does not always provide clear guidance for specific actions; what constitutes a virtue can be culturally relative.", bold_point_style))

    story.append(Paragraph("4. <b>Justice Theory (John Rawls, Aristotle):</b>", bold_point_style))
    story.append(Paragraph("This theory focuses on fairness, equity, and impartiality in the distribution of benefits and burdens, and in the administration of rules and procedures.", body_style))
    story.append(Paragraph("•   <b>Distributive Justice:</b> Concerns the fair distribution of society's resources and opportunities (e.g., Rawls' 'Veil of Ignorance' and 'Difference Principle' – inequalities are permissible only if they benefit the least advantaged).", bold_point_style))
    story.append(Paragraph("•   <b>Procedural Justice:</b> Concerns the fairness of processes used to make decisions and allocate resources.", bold_point_style))
    story.append(Paragraph("•   <b>Retributive Justice:</b> Concerns the fairness of punishments for wrongdoing.", bold_point_style))
    story.append(Paragraph("•   <b>Compensatory Justice:</b> Concerns fair compensation for past injustices or harm.", bold_point_style))
    story.append(Paragraph("•   <i>Critiques:</i> Different conceptions of 'fairness' exist; can be complex to apply.", bold_point_style))

    story.append(Paragraph("5. <b>Ethical Relativism vs. Ethical Absolutism/Universalism:</b>", bold_point_style))
    story.append(Paragraph("•   <b>Ethical Relativism:</b> Argues that morality is relative to the norms of one's culture or society. What is right in one culture may be wrong in another. There are no universal moral truths.", bold_point_style))
    story.append(Paragraph("    <i>Types:</i> Cultural Relativism, Subjectivism (morality is relative to the individual).", bold_point_style))
    story.append(Paragraph("•   <b>Ethical Absolutism/Universalism:</b> Proposes that there are universal moral principles that apply to everyone, everywhere, regardless of culture or individual beliefs (e.g., the UN Declaration of Human Rights leans towards this).", bold_point_style))
    story.append(Paragraph("    <i>Critiques of Relativism:</i> Can lead to moral paralysis or tolerance of harmful practices; makes moral progress difficult to define. Critiques of Absolutism: Can be seen as ethnocentric or insensitive to cultural context.", bold_point_style))

    story.append(Paragraph("<u>Conclusion:</u>", sub_heading_style))
    story.append(Paragraph("These major ethical theories provide diverse lenses through which to analyze and determine ethical behavior. In practice, individuals and organizations often draw upon a combination of these theories when making ethical decisions. An understanding of these frameworks is essential for entrepreneurs and business leaders to make responsible choices, build trust, and contribute positively to society. No single theory is universally accepted as perfect, but each offers valuable insights into the complex nature of morality.", body_style))

    story.append(Paragraph("Memory Trick: 'Can Do Very Righteous Justice Always?' (Consequentialism/Utilitarianism, Deontology/Kantian, Virtue Ethics, Rights Theory, Justice Theory, [Ethical] Relativism/Absolutism).", memory_trick_style))
    story.append(Paragraph("Diagram Suggestion: A table comparing the theories based on their focus (consequences, duty, character, rights, fairness), key proponents, and a simple guiding question for each (e.g., Utilitarianism: 'What action yields the greatest good?').", diagram_suggestion_style))

    story.append(Paragraph("Key Points to Expand Further:", expand_points_style))
    story.append(Paragraph("• Apply these theories to a specific business ethical dilemma (e.g., child labor in supply chains, environmental pollution, misleading advertising).", body_style))
    story.append(Paragraph("• Discuss the role of professional codes of ethics and how they relate to these theories.", body_style))
    story.append(Paragraph("• Explore the concept of 'stakeholder theory' in business ethics and its connection to utilitarian and rights-based approaches.", body_style))
    story.append(Spacer(1, 1*cm))

    # --- Build PDF ---
    try:
        doc.build(story)
        print(f"PDF generated successfully: {output_path}")
    except PermissionError:
        print(f"Error: Permission denied to write to '{output_path}'.")
        print("Please check file permissions or try saving to a different directory.")
    except Exception as e:
        print(f"An error occurred while generating the PDF: {e}")

if __name__ == '__main__':
    generate_exam_solutions_pdf()
