import os
import time

import openai
from langchain import LLMChain

openai.api_key = os.getenv("OPENAI_API_KEY")

from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.prompts import (
    AIMessagePromptTemplate,
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain.text_splitter import CharacterTextSplitter

prompt = """
Given the following list of job titles, assign each job title a score from 0 to 10 based on how likely the job would be to be in charge of hiring database administrators. Only return jobs with a score of over 9.

```
Service Writer
Bowman
Maintenance Planner
Pest Controller Assistant
Career Portals Teacher
Desktop Publishing Associate
Tentmaker
Detention Officer
Public Service Representative (PSR)
Human Resources Officer
Isotope Hydrologist
Cause Analyst
Florist
Battery Technician
Piano Teacher
Microbiologist
Institutional Research Director
Illustrator
Crop Specialist
Comprehensive Ophthalmologist
Litigation Assistant
Manager of Loss Prevention Operations
Process Control Engineer
Combat Engineer
Health Insurance Specialist
Information Technology Instructor (IT Instructor)
Maintenance Coordinator
Massage Therapist and Master Esthetician
Rehabilitation Assistant
Special Education Teaching Assistant
T Rail Turner
Fresh Work Inspector
Assistant State Attorney
Golf Course Manager
Journalism Instructor
Castings Trimmer
Transcriptionist
Marine Equipment Machinery Maintenance Mechanic
Analytical Chemist
Hardware Design Engineer
Grants Administrator
District Engineer
Operational Intelligence Officer (Management)
Diffusion Furnace Operator
Nanny
Media Planner
Activity Coordinator
Lead Fire Protection Engineer
Patriot Missile Air Defense Artillery
Director, Medical Writing
Match Marker
Communications Manager
Program Officer
Network Support Manager
Dance Teacher
Commissioning Engineer
Senior Stack Engineer
Mechanical Electrical Plumbing Supervisor (MEP Supervisor)
Health Information Systems Technician
Fraud Analyst
Database Administrator (DBA)
Machine Shop Pantograph Machine Operator
Product Marketing Manager
Scout
Table Games Dealer
Power System Electrical Engineer
Community Health Nursing Educational Director
Identifier
Mitigation Supervisor
Volunteer Coordinator
Director, Product Safety
Operations Supervisor
Immunopathologist
Nuclear Technician Research and Development
Stakeholder Manager
Employment Research and Planning Director
Quality Control Microbiology Supervisor
Activity Director
Compound Mixer
Script Writer
Pigeon Fancier
Chemical Process Engineer
Completion Engineer
Distribution Center Manager
Director of Audience Generation, Search, & Analytics
Stitcher Around
Job Developer
Family Physician
Hospital Director
Director of Landscape Architecture and Planning
Broadband Installer
Grant Coordinator
Chief Nuclear Medicine Technologist
Knapsack Sprayer
Embroiderer
Biomedical Field Service Engineer
Accounts Payables Clerk
Quality Assurance Director (QA Director)
Historiographer
Residential Sales Rep (Solar Consultant)
Strategic Intelligence Officer
Gum Scoring Machine Operator
Welder-Manufacture
Product Development Scientist
Policeman
Alcohol and Drug Counselor
Computer Graphics Illustrator
Club Manager
Key Carrier
Osteopathy Doctor (DO)
International Relations Professor
Financial Economist
Machinery Dismantler
Working Supervisor
Scrum Master
Basketball Coach
Service Supervisor
Reconciliation Clerk
Water Safety Instructor (WSI)
Field Representative
Optometrist, President/Practice Owner
Biometrics Technician
Reinsurance Clerk
Raw Material Manager
Dancer
Biology Research Assistant
National Investigative Producer
Stereotyper
Dog Trainer
Network Consultant
Welder/Installer
Youth Ministry Director
Maintenance Engineer
Customer Logistics Manager
Direct Response Consultant
Family Nurse Practitioner
Instructional Aide
Wireless Network Engineer
Touring Production Manager
Program Strategist
Athlete Marketing Agent
Loadmaster
Film Editor
Swimming Instructor
Record Producer
Employment Benefits or Pensions Retirement Plan Specialist
Music Therapy Teacher
Military Analyst
Visual Merchandising Specialist
Computer Systems Support Specialist
Industrial Ecologist
Circulation Director
Electro-Mechanical Engineer
Scout-Sniper
Imagery Intelligence
Case Manager
Senior Engineer
Drafting Detailer
Client Service Representative
Delivery Supervisor
Chemical, Biological, Radiological, And Nuclear (CBRN) Officer
Founder
Shipper/Receiver
Secretary of State
Research Compliance Specialist
Humane Officer
Syrup Machine Laborer
Clinical Psychology Professor
Communications Equipment Installer
Student Advisor
Senior Advisory
Milk Pasteurizer
Visiting Nurse
Kitchen Hand
Office Assistant
Busboy
Veterinarian (VET)
Accredited Farm Manager (AFM)
Business Division Chair
Actress
Paramedic
Senior Scientist
Solar Installer
Preschool Special Education Teacher
Refinery Superintendent
Shoe Clerk
Truck, Car, and Bus Cleaner
Public Relations Studies Director
Class B Driver
County Commissioner
Communications Officer
Enterprise Sales Person
Foundation Program Director
Political Consultant
Oil Program Compliance Specialist
Facility Technician
Professional Nursing Assistant (PNA)
Field Superintendent
Kitchen Designer
Real Estate Site Analyst
Principal Secretary
Engineering Officer
Silver Solderer
Quality Director
Handy Man
Information Systems Technology Professor
Clinical Engineer
Warehouse Associate
Foreign Trade Teacher
Support Specialist
Evidence Technician
Human Resources Associate (HR Associate)
Mig Welder
Pharmacist in Charge, Owner (PIC, Owner)
US Customs and Border Protection Officer (US CBPO)
Business Intelligence Manager
Munitions Handler
Dentist/Owner
Information Security Manager
Crude Tester
Flux Mixer
Behavior Therapist
Art Gallery Director
High School Biology Teacher
Distribution Operations Manager
College or University Faculty Member
Park Worker
Technology and Engineering Teacher
Breakfast Attendant
Equity Trader
Mill Work
Floral Manager
Commercial Credit Head
Banana Carrier
Safety Equipment Testing Specialist
Typist
Quality Control Inspector
Certification and Selection Specialist
Clam Shucker
Information Coordinator
Biological Scientist
Credit Administrator
Conference Manager
Engineer
Hospice Aide
Public Information Specialist
Lead Technologist/Manager
Diagnostic Radiologist
Settlement Clerk
Nurse Manager
Utilities Customer Service Representative
Aerospace Control And Warning Systems, Manuel Systems
Wholesaler
Home Care Coordinator
Change Over
Security Agent
Lead Pharmacy Technician (Lead Pharmacy Tech)
Boatwright
Pizza Delivery
Golf Course Superintendent
Proprietary Trader
Antenna Installer
Car Supplier
Flight Engineer
Data Specialist
Three-Dimensional Art Instructor
Head of Outreach and Delivery Services
Deck Lid Fitter
Ash Collector
Engineering Project Manager
Character Impersonator
Data Storage Specialist
Travelers' Aid Worker
State Trooper
Sports Information Director
Research and Development Technician
Production Scheduler
Institutional Advancement Vice President
Employee's Representative
Dog Sitter
Dietetic Intern
Chief Operating Officer (COO)
Electromechanical Assembly Technician
Airport Manager
Admin Assistant
Ventriloquist
Home Visitor - Home Base Head Start
Defect Cutter
Public Events Facilities Rental Manager
Catalog Librarian
Test Technician
Associate Product Integrity Engineer
Reading Teacher
Private Statistical/Psychometric Consultant
Child and Family Services Worker
Poultry Slaughterer
Commercial Floor Covering Installer
Computer Engineer
Timekeeper
Network Technology Instructor
Business Office Manager
Mammalogist
Dyer
Cattleman
Human Resources Generalist
Greenhouse Florist
Operations Coordinator
Scientific Technical Writer
Breakfast Cook
Layer
Credit Office Manager
Implant Coordinator
Dispute Resolution Specialist
Unloader
Go Go Dancer
Store Shopper
3D Animator
Boiler Attendant
Domestic Helper
Environmental Protection Specialist
Senior Hardware Engineer
Stewarding Supervisor
Loop Sewer
Diabetes Educator
Fire Investigator
Deputy Fire Marshal
Admissions Representative
Customer Support Analyst
Ultra Sound Technician
Lumberman
Activity Therapy Specialist
Computing Tutor
Respiratory Therapist (RT)
Graphic Designer/Production
Occupational Therapy Co-Director
Snap Shearer
Ophthalmic Photographer
Billboard Erector
Master Technician
Counselor at Law
Communication Manager
Accounting/Finance Tutor
Marble Installer
Product Test Specialist
Digital Retoucher
Networking Engineer
Web User Experience Strategist
Engineer of System Development
College Director
Taxonomist
Clinical Research Manager
Human Factors Engineer
Guest Services Manager
Environmental, Health, and Safety EHS Leader
Pediatrician, Managing Partner
City Auditor
Pawn Broker
Recruiter
Accounting Specialist
Seafood and Service Meat Manager
Galvanizer
Breeding Technician
Computer-Aided Design Technician (CAD Technician)
Sub Prior
Large Animal Husbandry Technician
Special Services Agent
Principal Architect
Book Keeper
Meeting Planner
Electrotherapist
Reviewer Sales
Route Driver
Heavy Equipment Plumbing Supervisor
Gas Processing Plant Operator
Operations Specialist
Student Admissions Clerk
Youth Coordinator
Water Resources Program Director
Claims Representative
Mechanotherapist
Event Decorator and Designer
Forge Operator
Computer Consultant
Club Attendant
Technical Support Representative
Warehouse Lead
Director of Catering
Carrier
Fine Arts Model
Terra Cotta Mason
Design Analyst
Service Manager
Law Secretary
Boot Maker
Saxophone Player
Tube Pusher
Executive Editor
Mathematics Teacher
Remote Encoding Operations Supervisor
Child Psychiatrist
CPS Team Lead (Chip Placement Solution Team Lead)
Advertising Account Executive
Welder-Fabricator
Display Advertising Sales Representative
Golf Professional
Bottle Washer
Skills Trainer
Mortgage Broker
Gunsmith
Street Contractor
Game Designer/Creative Director
Victim Witness Administrator
Electrical Power Station Technician
Media Director
Assistant Operator
Co-Supervisor Grounds and Landscape
Doctor (Dr)
Structural Steel Erection Supervisor
Knife Grinder
Rand Cementer
Window Cleaner
Day Spa Manager
Procedure Analyst
Power Plant Operators Supervisor
Customer Care Specialist
Pot Washer
Operations and Maintenance Supervisor (O&M Supervisor)
Hood Fitter
Examination Proctor
Product Developer
Game Developer
Certified Dietary Manager (CDM)
Payment Collector
Chiropractic Care
Title Agent
Epidemiologist
Retail Assistant Manager
Warehouse Coordinator
Consulting Engineer
Stress Engineer
Accounting Analyst
Studio Model
Cotton Opener
Purchasing Administrator
Supply Planner
Equipment Specialist
Cinematographer
Fashion Editor
Airline Captain
Nursing Instructor
Audiologist
Program Research Specialist
Black Bear Project Leader
Stringer
Department Director
Transport Engineer
Certified Nurse Aide (CNA)
Human Resources Information System Director (HRIS Director)
Consumer Studies Professor
Antique Dealer
Certificate of Clinical Competence in Audiology Licensed Audiologist (CCC-A Licensed Audiologist)
Customer Engagement Manager
Assistant Professor of Religion
Enrollment Services Dean
Repairer
Electronic Specialist
Bright Cutter
General Internist and Physician Leader
Circuit Design Engineer
Program Manager
Free Lance Model
Clam Digger
Envelope Stuffer
Hair Dresser
Law Clerk
Ceramic Designer
Exchange Operator
Client Services Manager
Vice President for Philanthropy
Weir Fisher
Food Stylist
Infant Teacher
Head of Systems Applications Programming
Patient Care Associate
Chief Engineer
Patient Care Specialist
Air Sampling and Monitoring
ESL Teacher (English as a Second Language Teacher)
Cryptologic Digital Network Technician/Analyst
Cleaning Supervisor
Department Chair
Field Artillery Officer
Traffic Supervisor
Taker Away
Lead Radiation Therapist
Curatorial Assistant
Outbound Supervisor
Construction Worker
Wireline Operator
Facilities Director
Evaporator
Traveler Changer
Harnessmaker
Line Lead
Resume Writer
School Coordinator
Grain Elevator Operator
Service Coordinator
Product Support Consultant
Geodesist
User Support Analyst
Engineering Production Liaison
Material Handler
Care Manager
Industrial Designer
Pay-Per-Click Strategist (PPC Strategist)
Service Superintendent
Title I Assistant
Object-Oriented Programmer
Transition Advisor
Compact Assembler
Activist
Segment Block Layer
Document Control Specialist
Reconstructive Surgeon
Judge
Digital Media Producer
Math Tutor
Sales Team Leader
Literary Agent
Jack
Electrical Assistant
Disability Specialist
Pharmaceutical Engineer
Tissue Technologist
Wireless Technician
Cruise Director
Quality Assurance QA Lab Technician
Oral Surgery Assistant
Web Analyst
Therapeutic Dietitian
Staff Development Coordinator
Information Architect
Structures Technician
Systems Development Manager
Tourist Agent
Distribution Coordinator
Checker/Stocker
Transport Medic
Quality Assurance Manager (QA Manager)
Staffing Associate
Home Theater Experience Expert
Plant Superintendent
Slot Ambassador
Stress Analyst
School Photographer
Naval Engineer
Contemporary English Literature Professor
Director of Entertainment
Licensed Insurance Sales Agent
Manager of Selection and Assessment
Vice Principal
Student Teaching Coordinator
Youth Worker
Costume Designer
Accounting Officer
Food Consultant
Tenant Selector
Tool and Equipment Rental Clerk
Power Plant Operations Manager
Course Developer
Congressional Assistant
Coordinator of Library Services
Promoter
Renewable Energy Project Manager
Food Preparer
Watermaster
Operating Systems Specialist
Cultivator
Four-H Agent
Enlisted Advisor
Glass Science Engineer
Clinical Molecular Genetics Laboratory Director
Home Health Aide (HHA)
Business Executive
Veterinary Surgeon
Specialty Food Products Supervisor
Precinct Captain
Organizational Consultant
Facilities Engineer
Early Head Start Director
Provider Scribe
Back Hanger
Wildlife Technician
Senior Certified Registered Nurse Anesthetist (Senior CRNA)
Compensation Analyst
Director of Compensation
5th Grade Teacher
Loan Specialist
Information Technology Technician (IT Technician)
Security Director
Pest Control Technician
Library Supervisor
Workforce Development Vice President
Director of Academic Support
Telecommunication Engineer
Learning Resources Assistant
Territory Supervisor
Web Specialist
Professor of Mathematics and Computer Science
Hotel General Manager
Exterminator
Floorperson
Plant Operator/Shift Supervisor
Supervisory Information Technology Specialist (Supervisory IT Specialist)
Project Manager, Senior
Shuttle Driver
Energy Trading Analyst
Faith Doctor
Stay Cutter
Health Plan Specialist
Sous Chef
Exec. Creative Director
Loss Control Consultant
Photographer
Web Engineer
Blindmaker
Technical Operations Vice President
Flight Service Agent
Editorial Writer
Schedule Supervisor
Agricultural Mechanic
Museum Security Chief
Assembly Member
Learning Manager
Information Technology Project Manager
Fabrication and Layout Craftsman
Commuter Pilot
Radiological Health Specialist
Referee
Computer Hardware Technician
Prints and Drawings Curator
Operation Specialist
News Producer
Aoc Strategy Plans And Operational Assessment Officer
Global Logistics Analyst
Circulation Manager
Chef de Cuisine
Associate Dentist
Tipstaff
Coach (Career Transition and Performance)
Cigarette Seller
Crash, Fire, and Rescue Fire Fighter```
"""


# From the following list of job titles, give me the top 100 that are most likely to be in charge of purchasing software.

# Works well on gpt-4
# Return the following list of job titles along with a score from 0 to 10 based on how likely that job title is to be responsible for purchasing software. Skip job titles with below a 3 score.


# add line numbers at the beginning of each line in prompt
# prompt = "\n".join(
#     [f"{i+1}. {line}" for i, line in enumerate(prompt.split("\n"))]
# )

model = "gpt-4"
model = "gpt-3.5-turbo-16k"


llm = ChatOpenAI(
    temperature=0.0, model=model, openai_api_key=os.getenv("OPENAI_API_KEY")
)  # , verbose=True, max_retries=0)

# map_prompt = HumanMessagePromptTemplate.from_template(prompt)
# map_prompt = ChatPromptTemplate.from_messages([map_prompt])
map_prompt = ChatPromptTemplate.from_messages([("human", prompt)])
map_llm_chain = LLMChain(llm=llm, prompt=map_prompt, verbose=False)

t1 = time.time()
# map_llm_chain.run({})
map_llm_chain({})
t2 = time.time()

print("Ran via LLMChain in ", t2 - t1)

t1 = time.time()
map_results = openai.ChatCompletion.create(
    model=model, messages=[{"role": "user", "content": prompt}]
)
t2 = time.time()

print("ran via openai python api in  ", t2 - t1)
