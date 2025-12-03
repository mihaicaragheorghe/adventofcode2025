d%a:
	@python3 day$(shell printf "%02d" $*)/a.py

d%b:
	@python3 day$(shell printf "%02d" $*)/b.py

d%:
	@echo "Running Day $* - Part A:"
	@python3 day$(shell printf "%02d" $*)/a.py
	@echo ""
	@echo "Running Day $* - Part B:"
	@python3 day$(shell printf "%02d" $*)/b.py

all:
	@for day in $(shell seq 1 12); do \
		if [ -d day$$(printf "%02d" $$day) ]; then \
			$(MAKE) d$$day; \
			echo ""; \
		fi \
	done

.PHONY: help
help:
	@echo "Advent of Code 2025"
	@echo ""
	@echo "Usage:"
	@echo "  make d1a    - Run day 1, part a"
	@echo "  make d1b    - Run day 1, part b"
	@echo "  make d14a   - Run day 14, part a"
	@echo "  make d1     - Run both parts of day 1"