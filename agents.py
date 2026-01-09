"""
agents.py - Component of the Clinical Trial Compliance Intelligence system.
Defines the specialized agents using a lightweight multi-agent pattern.
"""
import random
import time

class BaseAgent:
    def __init__(self, name, role, goal):
        self.name = name
        self.role = role
        self.goal = goal

    def log(self, message):
        print(f"[{self.name} - {self.role}]: {message}")

class RegulatoryResearcher(BaseAgent):
    def __init__(self):
        super().__init__(
            name="ReguBot",
            role="Regulatory Compliance Researcher",
            goal="Extract and summarize relevant FDA and EMA regulations for specific clinical trial domains."
        )

    def perform_research(self, trial_domain):
        self.log(f"Searching for regulations related to: {trial_domain}...")
        time.sleep(1)
        # Mocking regulatory data
        regulations = [
            {"id": "FDA-21-CFR-50", "body": "Protection of Human Subjects", "risk_level": "High"},
            {"id": "FDA-21-CFR-56", "body": "Institutional Review Boards", "risk_level": "Medium"},
            {"id": "EMA-GCP-R2", "body": "Good Clinical Practice Guidelines", "risk_level": "High"},
            {"id": "GDPR-Health", "body": "Patient Data Privacy Standards", "risk_level": "High"}
        ]
        self.log(f"Found {len(regulations)} relevant regulatory frameworks.")
        return regulations

class ProtocolAnalyzer(BaseAgent):
    def __init__(self):
        super().__init__(
            name="ProtoScan",
            role="Trial Protocol Auditor",
            goal="Analyze the clinical trial protocol for potential compliance gaps."
        )

    def analyze_protocol(self, protocol_text, regulations):
        self.log("Analyzing protocol sections against retrieved regulations...")
        time.sleep(1.5)
        findings = []
        for reg in regulations:
            score = random.uniform(0.7, 0.98) # Mocking compliance score
            gap_found = random.choice([True, False, False, False]) # Low probability of gap
            findings.append({
                "regulation_id": reg["id"],
                "compliance_score": score,
                "gap_detected": gap_found,
                "evidence": "Observed protocol section 4.2 matches requirements." if not gap_found else "Missing specific informed consent clause."
            })
        self.log(f"Audit complete. Compliance score distribution: {[f['compliance_score'] for f in findings]}")
        return findings

class ComplianceSynthesizer(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Syntho",
            role="Compliance Risk Synthesizer",
            goal="Summarize findings into a professional executive report with risk scores."
        )

    def generate_report(self, findings):
        self.log("Synthesizing analysis into executive summary...")
        time.sleep(1)
        total_score = sum(f["compliance_score"] for f in findings) / len(findings)
        critical_gaps = [f for f in findings if f["gap_detected"]]
        
        report = {
            "overall_health_score": total_score,
            "status": "APPROVED" if total_score > 0.85 and not critical_gaps else "NEEDS REVIEW",
            "findings_count": len(findings),
            "critical_violations": len(critical_gaps),
            "summary": f"Audit processed successfully with an average compliance of {total_score:.2%}. {len(critical_gaps)} critical gaps identified."
        }
        self.log(f"Final Report Status: {report['status']}")
        return report
