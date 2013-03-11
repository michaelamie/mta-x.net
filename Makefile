.PHONY: clean
clean:
	@echo "Removing Python bytecode (*.pyc) files..."
	@find . -name '*.pyc' -type f -print0 | xargs -0 rm