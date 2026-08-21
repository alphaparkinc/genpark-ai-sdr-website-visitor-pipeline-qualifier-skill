from client import AiSdrWebsiteVisitorPipelineQualifierClient

def main():
    client = AiSdrWebsiteVisitorPipelineQualifierClient()
    res = client.qualify_visitor("vertexsystems.com", "/pricing")
    print(f"Identified: {res['identified_company']['name']} ({res['identified_company']['headcount']} employees, {res['identified_company']['industry']})")
    print(f"Pipeline Fit Score: {res['pipeline_fit_score']}/100")
    seq = res["outreach_sequence_triggered"]
    print(f"Outreach Triggered: {seq['channel']} | Template: {seq['template']}")
    print(f"Message Preview: {seq['first_message_preview']}")

if __name__ == "__main__":
    main()
