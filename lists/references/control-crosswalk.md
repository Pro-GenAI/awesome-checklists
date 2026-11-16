# Control-level standards crosswalk (starter)

**Verified identifiers and proposed mappings:** 2026-11-15. The machine-readable [control-crosswalk.json](control-crosswalk.json) contains **22 candidate internal-to-external pairs** spanning OWASP ASVS, NIST CSF 2.0, ISO/IEC 27002:2022 and AICPA SOC 2 Trust Services Criteria. **External control identifiers were checked against primary-source publications.** The *relationship* between an awesome-checklists prompt and each external requirement is **topic-level and partial, not independently certified equivalence**. Many external clauses require controls beyond the linked internal check. This is a non-exhaustive sample of the 4,204-check library, not a completed standards audit.

## Why the distinction matters

- **Identity does not imply coverage:** `SEC-007` is about technical authorization. ASVS `v5.0.0-8.2.1` and `v5.0.0-8.2.2` have related security outcomes, but a `PASS` on `SEC-007` does not establish compliance with either ASVS requirement, nor does it prove the rest of ASVS was reviewed.
- **Levels are framework-specific:** ASVS `L1/L2/L3` describe the requirements of that standard; source checklist `P0/P1/P2` are contextual review priorities and have no equivalence.
- **NIST CSF outcomes are broader:** For instance, `PR.AA-05` covers an organization's access-permission management, which a project code test alone cannot demonstrate.
- **ISO and SOC 2 require scope and full-source review:** ISO/IEC 27002 provides control guidance used with ISO/IEC 27001 Annex A/Statement of Applicability, not ISO certification. AICPA SOC 2 criteria require independent audit evidence over the relevant system and review period; two candidate CC references are not a SOC 2 report.
- **No automated legal conclusions:** The crosswalk has no jurisdiction, processing purpose, legal basis, evidence or evaluated scope. Those must be recorded per product/release by qualified reviewers.

## Representative verified external IDs

| Source checklist | External reference | Relation requiring separate evidence |
| --- | --- | --- |
| `SEC-007` | OWASP ASVS **v5.0.0-8.2.1 / 8.2.2** (L1) | Function- and object-level authorization; source checklist also covers tenant and action boundaries |
| `SEC-009` | OWASP ASVS **v5.0.0-7.3.1 / 7.3.2** (L2) | Inactivity and absolute session lifetimes, independently verified |
| `SEC-103` | OWASP ASVS **v5.0.0-11.4.2** (L2) | Password hashing / KDF parameters |
| `SEC-111` | OWASP ASVS **v5.0.0-7.4.1** (L2) | Terminated sessions must no longer be usable |
| `SEC-118` | OWASP ASVS **v5.0.0-1.2.4** (L1) | Proposed partial mapping: database query injection prevention; requires a real query-sink test |
| `SEC-007` | NIST CSF 2.0 **PR.AA-05** | Access authorization and least privilege organizational outcome |
| `SEC-021` | NIST CSF 2.0 **PR.DS-02** | Protection of data in transit, beyond the specifics of TLS configuration |
| `SEC-031` | NIST CSF 2.0 **RS.MA-01** | Incident-response management, beyond the existence of a plan |
| `SEC-007` | ISO/IEC 27002:2022 **5.15** | Access control guidance, not evidence of ISO 27001 certification |
| `SEC-032` | ISO/IEC 27002:2022 **8.8** | Management of technical vulnerabilities |
| `SEC-007` | AICPA TSC **CC6.1** | Logical access protection across the scoped system |
| `SEC-035` | AICPA TSC **CC7.2** | Monitoring and analysis of security-relevant anomalies |

## Primary-source registers

1. [OWASP ASVS 5.0.0 English requirements CSV](https://github.com/OWASP/ASVS/blob/master/5.0/docs_en/OWASP_Application_Security_Verification_Standard_5.0.0_en.csv). Pin IDs to the exact **v5.0.0-** prefix and review the associated L1/L2/L3 value.
2. [NIST OSCAL machine-readable CSF 2.0 catalog](https://github.com/usnistgov/oscal-content/blob/main/nist.gov/CSF/v2.0/yaml/NIST_CSF_v2.0_catalog.yaml). The verified IDs use NIST CSF **2.0**, not withdrawn 1.1 identifiers.
3. [ISO/IEC 27002:2022 official standard preview](https://www.iso.org/standard/75652.html). Public section names/identifiers can be confirmed, but **licensed full control text** and the organization's ISO/IEC 27001 Statement of Applicability remain necessary.
4. [AICPA Trust Services Criteria official publication](https://us.aicpa.org/content/dam/aicpa/interestareas/frc/assuranceadvisoryservices/downloadabledocuments/trust-services-criteria-redlined.pdf). CC6.1 and CC7.2 were checked there; confirm the **applicable licensed edition and audit period** before making examination claims.

## How to expand it

For each candidate mapping, identify exact framework version, external ID, applicable scope, *what additional tests the external requirement needs*, current evidence, assigned subject-matter reviewer, applicable level/category, and resulting **verified / partial / rejected / N/A** decision. Keep the machine-readable mapping_status as `proposed-partial-topic-alignment` until that professional review has taken place. Verify new external IDs in the official source and record the URL and date; do not invent plausible-looking IDs or assume every internal check has a standards counterpart.

The broader [jurisdiction and compliance topic guide](compliance-crosswalk.md) remains useful for GDPR, India DPDP and other legal obligations. Neither crosswalk replaces law-specific professional analysis or a qualified independent assurance engagement.
