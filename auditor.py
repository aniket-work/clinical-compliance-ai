import os
import json
from typing import List, Dict
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

class ComplianceAuditor:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o", temperature=0)
        self.regulations = self._load_regulations()

    def _load_regulations(self) -> List[Dict]:
        with open("regulations.json", "r") as f:
            return json.load(f)

    def audit_protocol(self, protocol_text: str) -> List[Dict]:
        results = []
        for reg in self.regulations:
            # Simulation mode for the PoC to ensure it runs without an API key
            # In a production scenario, this block would use the self.llm call
            audit_result = {
                "rule_id": reg["id"],
                "category": reg["category"],
                "status": "Compliant",
                "justification": f"The protocol's section on {reg['category']} matches the regulatory requirements defined in {reg['id']}.",
                "risk_level": reg["risk_level"]
            }
            
            # Specific logic for the mock to show variety
            if "Informed Consent" in reg['category'] and "CFR" not in protocol_text:
                audit_result["status"] = "Non-Compliant"
                audit_result["justification"] = "Protocol lacks explicit reference to FDA 21 CFR Part 50 as required."
            elif "Safety" in reg['category'] and "timeline" not in protocol_text.lower():
                audit_result["status"] = "Partial"
                audit_result["justification"] = "Adverse event reporting is mentioned but without specific timelines."
            
            results.append(audit_result)
        return results

if __name__ == "__main__":
    with open("protocol_mock.md", "r") as f:
        protocol = f.read()
    
    auditor = ComplianceAuditor()
    audit_findings = auditor.audit_protocol(protocol)
    
    print(json.dumps(audit_findings, indent=2))
    with open("audit_results.json", "w") as f:
        json.dump(audit_findings, f, indent=2)
