.PHONY: test test-verbose coverage clean lint install dev-install

# Python executable
PYTHON := python3
# Test directories
TEST_DIR := tests/
# Coverage report directory
COVERAGE_DIR := coverage_reports/

install:
	$(PYTHON) -m pip install -e .

dev-install:
	$(PYTHON) -m pip install -e ".[dev]"

test:
	$(PYTHON) -m pytest $(TEST_DIR)

test-verbose:
	$(PYTHON) -m pytest -v $(TEST_DIR)

coverage:
	$(PYTHON) -m pytest --cov=scribe $(TEST_DIR) --cov-report=html:$(COVERAGE_DIR)
	@echo "Coverage report generated in $(COVERAGE_DIR)"

lint:
	$(PYTHON) -m flake8 project/ tests/
	$(PYTHON) -m black --check project/ tests/
	$(PYTHON) -m isort --check-only project/ tests/

format:
	$(PYTHON) -m black project/ tests/
	$(PYTHON) -m isort project/ tests/

clean:
	rm -rf $(COVERAGE_DIR)
	rm -rf .coverage
	rm -rf .pytest_cache
	rm -rf **/__pycache__
	rm -rf *.egg-info