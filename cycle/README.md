# Credit thesis cycle

Runs every 2 days at 07:10 (odd days of the month) from cron. Tag in crontab: `# credit-thesis-cycle`.

## What one run does
1. collect: reads recent posts of the accounts in `accounts.txt` through Chrome. Read only.
2. merge: `merge_x.py` adds new posts to `../corpus/x/<handle>.md`. No model.
3. readings: `fred_pull.py` pulls spreads and rates from FRED. No model.
4. analyse: updates the evidence, the skill sweep, the scenario grid and the memo in `../runs/<date>/`. See "Memo files and house style".
5. view: `build_view.py` writes the one-page view `view.html` into the run directory. No model.
6. publish: optional. Updates one published page from `view.html`. Off unless the file `publish.enabled` exists.
7. send: mails `email.txt` to the addresses in `recipients.txt`. One mail per run.

## The one-page view
- `build_view.py <run_dir> <out.html>` builds the page. Every number comes from `readings.json`, `scenarios.json` and the grid script.
- `build_view.py --check <run_dir>` validates the inputs. It prints PASS or FAIL with reasons, and compares the chart numbers with `report.md`.
- `view.json`, in the run directory, holds the text that only the analysis can supply. The analyse stage writes it. `view_schema.md` defines it.
- If `view.json` is missing or invalid, the page still has the axis scale, the scenario bar and the expected-move chart. One line says that the text was not updated.
- `fred_pull.py` now adds `month_before` and `month_before_date` to each reading. The expected-move chart uses them for the one-month move.
- `publish_prompt.md` and `publish-settings.json` run the publish stage. It can use only the Artifact tool and read `runs/**/view.html`.
- Switch publishing on with `touch publish.enabled` in this directory. Switch it off with `rm publish.enabled`.
- A build or publish failure is a warning in the log. It never stops the email.
- `*.bak2` files, and `fred_pull.py.bak`, hold the versions from before this change (2026-11-23).

## Memo files and house style
- `thesis_full.md`: the long working memo (ten parts, four gates). The next run reads it. It falls back to `thesis.md` when the previous run has no `thesis_full.md`.
- `thesis.md`: the styled memo, about 1,100 words plus 3 exhibits, written from `thesis_full.md`. `run_cycle.sh` finds the previous run by this file.
- `email.txt`: the styled email, plain text, about 900 words. Its first paragraph states what changed.
- `style_guide.md`: the house style. Edit it to change the style of every future memo and email.
- Humaniser passes: the analyse stage reads the `humanizer` and `avoid-ai-writing` skills and makes three passes on both styled files. It logs them in `styled/humaniser_log.md`.
- `check_numbers.py <styled file> <source file>...`: a script, not the model, checks that each number in a styled file is in `thesis_full.md`, `report.md` or `readings.json`. It prints PASS or FAIL. The sign is ignored and number words are not checked.
- If the check still fails after 3 tries, the first paragraph of the email says so.
- `*.bak` files hold the versions from before this change (2026-11-23).

## Needs
- The computer is on. Chrome is open with the Claude extension, logged in to X.
- Claude Code is signed in, with the Gmail connector.
- A previous run directory that holds `thesis.md`.

## Safety
- `guard_collect.py`: the browser can open only `https://x.com/<listed handle>` and can run only `collect.js`.
- `guard_send.py`: mail goes only to `recipients.txt`, no cc or bcc, one mail per run.
- The stage that reads posts cannot send mail. The stage that sends mail reads one file.

## Commands
- Test without mail: `run_cycle.sh --no-send`
- Corpus only: `run_cycle.sh --only-collect`
- Change accounts: edit `accounts.txt`
- Stop the job: `crontab -e`, delete the line that ends with `# credit-thesis-cycle`
- Log: `~/.local/state/credit-thesis-cycle/run.log`
