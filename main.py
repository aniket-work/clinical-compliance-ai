"""
main.py - Entry point for the Autonomous Clinical Trial Compliance Intelligence.
Orchestrates the multi-agent flow and analytics.
"""
from agents import RegulatoryResearcher, ProtocolAnalyzer, ComplianceSynthesizer
from utils import generate_compliance_stats
import json

def run_compliance_audit(protocol_summary):
    print("=== Starting Autonomous Clinical Compliance Audit ===")
    
    # 1. Initialize Agents
    researcher = RegulatoryResearcher()
    analyzer = ProtocolAnalyzer()
    synthesizer = ComplianceSynthesizer()
    
    # 2. Perform Research
    domain = "Infectious Diseases / Vaccine Trial"
    regulations = researcher.perform_research(domain)
    
    # 3. Analyze Protocol
    findings = analyzer.analyze_protocol(protocol_summary, regulations)
    
    # 4. Synthesize Report
    report = synthesizer.generate_report(findings)
    
    # 5. Output results
    print("\n=== Audit Results Summary ===")
    print(json.dumps(report, indent=4))
    
    # 6. Generate Statistical Visuals
    print("\nGenerating business performance statistics...")
    generate_compliance_stats()
    
    return report

if __name__ == "__main__":
    sample_protocol = "Phase III randomized trial for new respiratory vaccine. Participant age: 18-65. Expected cohort size: 5000."
    run_compliance_audit(sample_protocol)
