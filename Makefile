PROJECT_FILES = itineraries/
TEST_FILES = tests/

FORMATTER = black
LINTER = ruff
TYPE_CHECKER = mypy

.PHONY: c
c: code

.PHONY: code
code: code/fix code/check

.PHONY: code/fix
code/fix: code/lint-fix code/format

.PHONY: code/check
code/check: code/lint code/type code/format-check

.PHONY: code/type
code/type:
	$(TYPE_CHECKER) $(PROJECT_FILES) $(TEST_FILES)

.PHONY: code/lint
code/lint:
	$(LINTER) --no-fix $(PROJECT_FILES) $(TEST_FILES)

.PHONY: code/lint-fix
code/lint-fix:
	$(LINTER) --fix $(PROJECT_FILES) $(TEST_FILES)

.PHONY: code/format
code/format:
	$(FORMATTER) $(PROJECT_FILES) $(TEST_FILES)

.PHONY: code/format-check
code/format-check:
	$(FORMATTER) --check $(PROJECT_FILES) $(TEST_FILES)

.PHONY: test
test:
	pytest -v $(TEST_FILES)

.PHONY: run
run:
	uvicorn itineraries.main:app --reload

.PHONY: help
help:
	@echo ""
	@echo "General"
	@echo "-------"
	@echo "make help"
	@echo "    Show this help message."
	@echo ""
	@echo "Code quality tools"
	@echo "------------------"
	@echo "make code, make c"
	@echo "    Run all fixing targets and all checks."
	@echo "make code/fix"
	@echo "    Run all fixing targets (code/lint-fix, code/format)."
	@echo "make code/check"
	@echo "    Run all checks (code/lint, code/type, code/format-check)."
	@echo "make code/type"
	@echo "    Run static type checker."
	@echo "make code/lint"
	@echo "    Run linter (also runs isort check)."
	@echo "make code/lint-fix"
	@echo "    Run linter in fixing mode (also does isort work)."
	@echo "make code/format"
	@echo "    Format all files with standard formatter."
	@echo "make code/format-check"
	@echo "    Run check of formatting."
	@echo ""
	@echo "Tests"
	@echo "-----------------------"
	@echo "make test"
	@echo "    Run all tests locally."
	@echo ""
	@echo "App management"
	@echo "-----------------------"
	@echo "make run"
	@echo "    Run the project locally."
	@echo ""
