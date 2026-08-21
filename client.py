class AiSdrWebsiteVisitorPipelineQualifierClient:
    def qualify_visitor(self, visitor_company_domain: str, page_visited: str = "/pricing") -> dict:
        company = {
            "name": "Vertex Systems Inc.",
            "domain": visitor_company_domain,
            "headcount": 340,
            "industry": "FinTech",
            "hq": "New York, USA",
            "tech_stack": ["AWS", "Postgres", "React", "Stripe"]
        }
        sequence = {
            "trigger": "IMMEDIATE",
            "channel": "email + linkedin",
            "template": "high_intent_pricing_visitor_v3",
            "first_message_preview": "Hi [FirstName], noticed your team at Vertex Systems was exploring our enterprise pricing..."
        }
        return {
            "identified_company": company,
            "pipeline_fit_score": 94.5,
            "outreach_sequence_triggered": sequence
        }
