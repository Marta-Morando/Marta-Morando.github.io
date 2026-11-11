# Marta-Morando.github.io

## Research analytics

The website uses the existing GA4 stream `G-Q6Y02FCWKZ`. Research interactions are
sent by `analytics.js` through the existing Google tag. Open the
[Marta Morando Analytics property](https://analytics.google.com/analytics/web/#/a275155640p390996833/reports/intelligenthome).

| Event | What is counted |
| --- | --- |
| `jmp_paper_click` | A click on the JMP title or paper button |
| `jmp_abstract_open` | Expanding the JMP abstract |
| `jmp_bibtex_click` | Clicking the JMP BibTeX button |
| `polarizedtech_paper_click` | A click on the Polarized Technologies title or paper button |
| `polarizedtech_abstract_open` | Expanding its abstract |
| `polarizedtech_bibtex_click` | Clicking its BibTeX button |
| `polarizedtech_slides_click` | Clicking its slides link |
| `geography_abstract_open` | Expanding the Geography abstract |
| `geography_paper_click` | A click on the Geography title or paper button |
| `geography_bibtex_click` | Clicking the Geography BibTeX button |
| `ai_interview_abstract_open` | Expanding the AI interviews abstract |
| `contributive_justice_abstract_open` | Expanding the Contributive Justice abstract |
| `cv_click` | Clicking the CV link |

### View a JMP readership report

These are custom **event names**, so no custom dimensions need to be registered.
The following report setup is a recipe; it does not create a saved report by itself.

1. In Analytics, open **Explore > Blank** and name the exploration **JMP readership**.
2. Import dimensions **Event name**, **Country**, **Town/City** (or **City**),
   **Session source / medium**, **Device category**, and **Date**.
3. Import metrics **Event count** and **Total users**.
4. Add **Country** to Rows, and both metrics to Values. Add a filter:
   **Event name exactly matches `jmp_paper_click`**.
5. Duplicate the tab and replace Country with **Session source / medium** for
   referral sources, **Device category** for devices, or **Date** for daily clicks.
   An optional Town/City tab shows approximate locations.
6. For an interaction overview, use **Event name** as Rows and change the filter
   to **Event name begins with `jmp_`**. This separates paper clicks, abstract
   opens, and BibTeX clicks.

The Realtime report can show incoming events shortly after they occur. Standard
reports can take 24-48 hours to process new data. The report's Total users metric
counts Analytics users, not verified distinct people.

### Interpretation

- Collection begins after deployment; these custom events cannot reconstruct past clicks.
- A paper click measures an attempt to open the PDF from this website, not proof
  that the person read it, completed the download, or spent a particular time reading.
- Direct visits to a PDF URL, shared PDF attachments, and context-menu opens are
  not captured by this website click handler. Blockers and consent settings can
  also reduce the observed counts.
- Analytics provides aggregate location, acquisition, and device information. It
  does not identify readers by name, email address, or university. Geography is approximate.
- If enhanced measurement already emits `file_download`, it may describe the same
  click. Do not add that count to `jmp_paper_click`; filter by the desired event.
- The custom events contain only fixed action names and, for PDF links, public
  document URLs without query strings or fragments. No reader identity is added.

Google documentation: [custom events](https://developers.google.com/analytics/devguides/collection/ga4/events),
[enhanced measurement](https://support.google.com/analytics/answer/9216061),
[geographic reporting](https://support.google.com/analytics/answer/12948931).
