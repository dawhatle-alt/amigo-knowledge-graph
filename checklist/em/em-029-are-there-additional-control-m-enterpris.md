---
name: em-029-are-there-additional-control-m-enterpris
type: checklist-item
component: em
section: "Control-M/Enterprise Manager Technical Concerns"
answer_type: yes-no
answer_options: ["Yes", "No"]
tsa_answer_options: ["Advised", "Not Applicable"]
blocking: false
related_rules: []
related_components: ["aapi", "application-integrator", "bim", "forecast", "mft", "self-service", "wcm", "workflow-insights", "workload-archiving"]
hcu_sources: ["[[EM-Services]]"]
extractors: [X21]
status: active
source_sheet: "AMIGO EM Checklist V22"
source_row: 29
source_file: AMIGO_Checklist_V22_20251030.xlsx
---

# Are there additional Control-M/Enterprise Manager Add-on components?

## Question

Are there additional Control-M/Enterprise Manager Add-on components?

## TSA guidance

Review the below for known issues / KA fi required

## Items

- **Control-M Batch Impact Manager** → [[bim]]
- **Control-M Forecast** → [[forecast]]
- **Control-M Workflow Insights** → [[workflow-insights]]
  - Customer: If using Control-M Workflow Insights, do review the below knowledge article. 000425199 - FAQ for Control-M Workflow Insights
- **Control-M Workload Archiving Server** → [[workload-archiving]]
  - Customer: If using Control-M Workload Archiving Server, do review the below knowledge article. 000208315 - FAQ: Questions for Control-M Workload Archiving (including Control-M for z/OS)
- **Control-M Automation API (AAPI)** → [[aapi]]
  - TSA: If the Control-M AAPI is being upgraded too, CTM CLI will need to be updated too
- **Control-M Self Service** → [[self-service]]
- **Control-M Workload Change Manager** → [[wcm]]
- **Control-M Application Intergrator** → [[application-integrator]]
- **Control-M Manage File Transfer** → [[mft]]

## Related

- Component: [[aapi]]
- Component: [[application-integrator]]
- Component: [[bim]]
- Component: [[forecast]]
- Component: [[mft]]
- Component: [[self-service]]
- Component: [[wcm]]
- Component: [[workflow-insights]]
- Component: [[workload-archiving]]
