from flask import Flask, request, jsonify
import random
app = Flask(__name__)

def generate_bullet_points():
    specialties_bullet_points = {
        "Med/Surg": [
            "Provided direct patient care on a busy medical/surgical unit.",
            "Assisted in the management of post-operative patients.",
            "Monitored and administered medications.",
            "Collaborated with interdisciplinary teams to develop patient care plans.",
            "Conducted patient education on recovery and self-care.",
            "Assessed and documented patient progress and needs.",
            "Implemented infection control protocols.",
            "Prioritized and managed multiple patient cases.",
            "Assisted in emergency procedures and rapid response teams.",
            "Promoted patient safety and fall prevention measures.",
        ],

            

        "Telemetry": [
            "Monitored patients with cardiac telemetry needs.",
            "Assessed cardiac rhythms and reported abnormalities.",
            "Administered intravenous medications.",
            "Educated patients and families on heart health.",
            "Coordinated care with cardiologists and cardiovascular nurses.",
            "Managed patients with heart failure and arrhythmias.",
            "Responded to cardiac emergencies and rapid response situations.",
            "Utilized EHR for comprehensive patient charting.",
            "Collaborated with healthcare teams for rapid patient assessments.",
            "Maintained patient confidentiality and privacy.",
        ],

        "Med/Surg Tele": [
            "Cared for patients with telemetry monitoring needs.",
            "Assessed cardiac rhythms and reported abnormalities.",
            "Administered intravenous medications.",
            "Educated patients and families on home care instructions.",
            "Coordinated care with telemetry nurses and cardiologists.",
            "Managed patients with heart failure and post-cardiac interventions.",
            "Responded to cardiac emergencies and arrhythmias.",
            "Utilized EHR for comprehensive patient charting.",
            "Collaborated with healthcare teams for rapid patient assessments.",
            "Maintained patient confidentiality and privacy.",
        ],
        "Stepdown": [
            "Managed patients transitioning from critical care to general care.",
            "Monitored vital signs and cardiac rhythms.",
            "Administered complex medications and titrations.",
            "Assisted in procedures and interventions.",
            "Provided comprehensive patient assessments.",
            "Collaborated with physical therapists for patient mobility.",
            "Utilized advanced EKG interpretation skills.",
            "Implemented critical care protocols in high acuity patients.",
            "Evaluated patient responses to treatments and interventions.",
            "Educated patients and families on recovery and medication management.",
        ],
        "ICU": [
            "Provided specialized care for critically ill patients.",
            "Managed ventilated patients and continuous hemodynamic monitoring.",
            "Administered intravenous drips and medications.",
            "Collaborated with healthcare teams to optimize patient outcomes.",
            "Conducted ongoing patient assessments and interventions.",
            "Assisted in emergency procedures and code blue responses.",
            "Prioritized care for unstable patients.",
            "Maintained infection control measures in isolation rooms.",
            "Utilized advanced life support skills.",
            "Managed patient and family emotional support during critical illness.",
        ],
        "CVICU": [
            "Cared for patients with complex cardiac conditions.",
            "Managed post-cardiac surgery patients.",
            "Administered cardiac medications and titrations.",
            "Assessed and monitored hemodynamic status.",
            "Collaborated with cardiologists and cardiac surgeons.",
            "Assisted in intra-aortic balloon pump management.",
            "Provided care for patients with ventricular assist devices.",
            "Assisted in cardiac procedures and interventions.",
            "Managed patients with heart failure and cardiac shock.",
            "Educated patients and families on cardiac health and self-care.",
        ],
        "Neuro ICU": [
            "Provided specialized care for patients with neurological conditions.",
            "Managed patients with traumatic brain injuries.",
            "Administered neurologic medications and titrations.",
            "Assessed and monitored intracranial pressure.",
            "Collaborated with neurologists and neurosurgeons.",
            "Assisted in lumbar punctures and intracranial pressure monitoring.",
            "Provided care for patients with strokes and seizures.",
            "Assisted in neurologic procedures and interventions.",
            "Managed patients with neuromuscular disorders.",
            "Educated patients and families on neurological care and therapies.",
        ],
        "Labor and Delivery": [
            "Provided care for expectant mothers throughout labor and childbirth.",
            "Monitored fetal heart rates and maternal vital signs.",
            "Assisted in natural deliveries and cesarean sections.",
            "Educated new mothers on postpartum care.",
            "Managed patients during high-risk pregnancies.",
            "Administered labor-inducing medications.",
            "Collaborated with obstetricians and midwives for delivery planning.",
            "Provided emotional support during labor and birth.",
            "Assessed and managed postpartum complications.",
            "Educated families on newborn care and breastfeeding.",
        ],
        "Interventional Radiology": [
            "Assisted in diagnostic and interventional radiological procedures.",
            "Monitored patients during imaging-guided interventions.",
            "Administered contrast agents and medications.",
            "Ensured patient safety during procedures.",
            "Collaborated with radiologists and technologists for optimal imaging.",
            "Assisted in biopsies and fluid aspirations.",
            "Provided post-procedure patient care and recovery.",
            "Educated patients on pre-procedure preparations.",
            "Managed and documented patient responses to interventions.",
            "Utilized radiation safety measures.",
        ],
        "Cath Lab": [
            "Assisted in diagnostic and interventional cardiac procedures.",
            "Monitored patients during angiograms and interventions.",
            "Administered medications and managed hemodynamic status.",
            "Collaborated with cardiologists and radiologists for optimal patient care.",
            "Assisted in pacemaker and defibrillator insertions.",
            "Managed patients during percutaneous coronary interventions.",
            "Assessed and managed complications during procedures.",
            "Operated specialized imaging and monitoring equipment.",
            "Provided post-procedure patient care and monitoring.",
            "Educated patients on post-procedure care and lifestyle changes.",
        ],
        "ED": [
            "Triage and assess patients presenting to the Emergency Department.",
            "Initiated interventions and treatments for various medical emergencies.",
            "Performed rapid assessments and initiated life-saving measures.",
            "Collaborated with healthcare teams to stabilize patients for admission or discharge.",
            "Managed trauma and resuscitation cases.",
            "Administered pain management medications.",
            "Conducted patient and family education on emergency care.",
            "Utilized EHR for efficient documentation.",
            "Maintained a safe and controlled environment in the ED.",
            "Participated in disaster preparedness and response.",
        ],
        "OR": [
            "Assisted in preoperative preparations and surgical set-up.",
            "Maintained sterile fields during surgeries.",
            "Operated specialized equipment and instruments.",
            "Ensured patient safety and infection control measures.",
            "Collaborated with surgical team members for optimal patient care.",
            "Monitored patient vitals during surgical procedures.",
            "Managed surgical instruments and supplies.",
            "Promoted a positive surgical environment.",
            "Provided emotional support to patients and families pre-operatively.",
            "Documented accurate and comprehensive surgical records.",
        ],
        "NICU": [
            "Provided specialized care for premature and critically ill newborns.",
            "Monitored vital signs and administered neonatal medications.",
            "Assisted in neonatal resuscitation.",
            "Collaborated with healthcare teams to promote infant development.",
            "Managed infants on ventilators and CPAP.",
            "Administered total parenteral nutrition (TPN).",
            "Maintained a sterile environment for high-risk infants.",
            "Provided kangaroo care and developmental support.",
            "Conducted family education on NICU care and needs.",
            "Collaborated in developmental follow-up and support.",
        ],
        "PICU": [
            "Cared for critically ill pediatric patients.",
            "Managed ventilated and hemodynamically unstable patients.",
            "Administered pediatric medications and therapies.",
            "Supported families during challenging times.",
            "Collaborated with pediatric specialists for comprehensive care.",
            "Assisted in pediatric resuscitation and code response.",
            "Utilized pain management techniques for pediatric patients.",
            "Provided play therapy and distraction techniques.",
            "Conducted family-centered care and communication.",
            "Monitored and managed pediatric medical devices.",
        ],
         "Endoscopy": [
            "Assisted in diagnostic and interventional endoscopic procedures.",
            "Monitored patients during endoscopy.",
            "Administered sedation and monitored patient response.",
            "Ensured patient safety and comfort during procedures.",
            "Collaborated with gastroenterologists and surgeons.",
            "Assisted in biopsy and specimen collection.",
            "Provided post-procedure patient care and recovery.",
            "Educated patients on pre-procedure instructions.",
            "Managed and documented patient responses to interventions.",
            "Utilized infection control and sterilization protocols.",
        ],
         "PACU": [
            "Managed post-anesthesia care for surgical patients.",
            "Monitored vital signs and airway patency.",
            "Administered post-operative medications and pain management.",
            "Assessed and managed patient recovery from anesthesia.",
            "Collaborated with surgical teams for patient handoff.",
            "Managed patients with varying surgical procedures.",
            "Responded to post-operative complications and emergencies.",
            "Provided emotional support to patients and families.",
            "Documented comprehensive patient recovery status.",
            "Ensured patient safety during the PACU stay.",
        ],
        "School Nurse": [
            "Provided health services to students and staff.",
            "Administered medications and treatments as needed.",
            "Conducted health screenings and assessments.",
            "Managed and documented student health records.",
            "Collaborated with teachers and parents on health-related concerns.",
            "Responded to medical emergencies and injuries.",
            "Implemented infection control and disease prevention measures.",
            "Developed health care plans for students with chronic conditions.",
            "Educated students and staff on health and wellness topics.",
            "Promoted a healthy and safe school environment.",
        ],
    }
    return specialties_bullet_points

@app.route("/bullet_points", methods=['GET'])
def get_bullet_points():
    bullet_points = generate_bullet_points()
    return jsonify(bullet_points)

def generate_random_bullet_points(unit):
    specialties_bullet_points = generate_bullet_points()
    all_bullet_points = specialties_bullet_points.get(unit, [])
    random.shuffle(all_bullet_points)
    return all_bullet_points[:4]
@app.route("/random_bullet_points/<unit>", methods=['GET'])
def get_random_bullet_points(unit):
    bullet_points = generate_random_bullet_points(unit)
    return jsonify(bullet_points)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)

