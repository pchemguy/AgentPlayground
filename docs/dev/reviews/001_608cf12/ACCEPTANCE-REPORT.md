# Runtime acceptance report

State: Pending. All 27 cases A-001 through A-027 remain Pending; no consumer execution or native transcript is claimed.

The machine-readable registry is [cases.json](acceptance/cases.json), governed by [case-record.schema.json](acceptance/case-record.schema.json). Assessor expectations belong in [acceptance/oracle](acceptance/oracle/README.md); actual execution records belong in [runs](runs/README.md). Support-tool verification is recorded separately in [SETUP-SUPPORT](acceptance/SETUP-SUPPORT.md).

Evidence stays on `evaluation/008-runtime-acceptance`. Never merge this branch into product main or expose its oracle/evidence to consumer agents. The protected API utility may be copied independently as explicitly authorized setup tooling; that does not authorize copying oracle or case evidence.
