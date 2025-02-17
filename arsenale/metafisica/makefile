# Variables passed from main makefile
PDF_OUTPUT ?= ../../tipografia
CACHE_DIR ?= ../../.cache
PROJECT ?= $(notdir $(CURDIR))

# Directory structure
MD_DIR = md
LATEX_DIR = latex
IMG_DIR = img
LAYOUTS_DIR = ../../_layouts

# Output files
PDF_FILE = $(PDF_OUTPUT)/$(PROJECT).pdf
TEX_FILE = $(LATEX_DIR)/$(PROJECT).tex
CLS_FILE = $(LAYOUTS_DIR)/gs-adonis.cls
CLS_LOCAL = $(LATEX_DIR)/gs-adonis.cls

# LaTeX template and tools
TEMPLATE = $(LAYOUTS_DIR)/tex2pdf.tex
PDFLATEX = pdflatex -interaction=nonstopmode
PANDOC = pandoc
GREP = grep
SED = sed

# File lists
MD_FILES = $(sort $(wildcard $(MD_DIR)/*.md))
INDEX_FILE = index.md
TEX_DEPS = $(wildcard $(LATEX_DIR)/*.tex)
IMG_DEPS = $(wildcard $(IMG_DIR)/*)

# Detect OS and set MD5 command
UNAME_S := $(shell uname -s)
ifeq ($(UNAME_S),Darwin)
    MD5_CMD = md5 -r
else
    MD5_CMD = md5sum
endif

# Cache management
CACHE_FILE = $(CACHE_DIR)/$(PROJECT).cache
MD5_FILE = $(CACHE_DIR)/$(PROJECT).md5

# Shell commands
MKDIR = mkdir -p
CP = cp
MV = mv
RM = rm -f
TOUCH = touch

# Extract title from index.md frontmatter
# This assumes the title is in the format: "title: My Title"
TITLE = $(shell if [ -f $(INDEX_FILE) ]; then \
            $(SED) -n '/^---/,/^---/p' $(INDEX_FILE) | \
            $(GREP) '^title:' | \
            $(SED) 's/^title:[[:space:]]*\(.*\)/\1/' | \
            $(SED) 's/^"\(.*\)"$$/\1/' | \
            $(SED) "s/^'\(.*\)'$$/\1/"; \
        else \
            echo "$(PROJECT)"; \
        fi)

# Function to check if files have changed
check_md5 = $(shell if [ -f $(MD5_FILE) ]; then \
                $(MD5_CMD) $(1) | diff $(MD5_FILE) - >/dev/null 2>&1 && echo "0" || echo "1"; \
            else \
                echo "1"; \
            fi)

.PHONY: all pdf clean force setup

# Default target
all: pdf

# Force rebuild regardless of changes
force: clean pdf

# Setup necessary files and directories
setup: $(CLS_LOCAL)
	@$(MKDIR) $(LATEX_DIR)

$(CLS_LOCAL): $(CLS_FILE)
	@echo "Copying LaTeX class file..."
	$(CP) $(CLS_FILE) $(CLS_LOCAL)

# PDF generation with smart recompilation
pdf: setup $(PDF_FILE)

# Generate TEX file from markdown
$(TEX_FILE): $(MD_FILES) $(TEX_DEPS) $(IMG_DEPS) $(CLS_LOCAL)
	@echo "Generating $(PROJECT).tex with Pandoc..."
	@echo "Using title: $(TITLE)"
	$(PANDOC) $(MD_FILES) \
		--template=$(TEMPLATE) \
		--listings \
		-V title="$(TITLE)" \
		-o $(TEX_FILE)
	$(MD5_CMD) $(MD_FILES) $(TEX_DEPS) $(IMG_DEPS) > $(MD5_FILE)

# Compile PDF
$(PDF_FILE): $(TEX_FILE)
	@echo "Compiling $(PROJECT).tex..."
	@cd $(LATEX_DIR) && \
	if $(PDFLATEX) $(PROJECT).tex > $(PROJECT).log 2>&1; then \
		if grep -q "Rerun to get" $(PROJECT).log || \
		   grep -q "LaTeX Warning: Label(s) may have changed" $(PROJECT).log || \
		   grep -q "LaTeX Warning: Reference" $(PROJECT).log; then \
			echo "References changed, rerunning..."; \
			$(PDFLATEX) $(PROJECT).tex > $(PROJECT).log 2>&1; \
			if grep -q "Rerun to get" $(PROJECT).log; then \
				echo "Final pass..."; \
				$(PDFLATEX) $(PROJECT).tex > $(PROJECT).log 2>&1; \
			fi \
		fi \
	else \
		echo "Error in LaTeX compilation. Check $(LATEX_DIR)/$(PROJECT).log"; \
		exit 1; \
	fi
	@if [ -f "$(LATEX_DIR)/$(PROJECT).pdf" ]; then \
		$(MV) $(LATEX_DIR)/$(PROJECT).pdf $(PDF_OUTPUT)/; \
		echo "PDF generated successfully: $(PDF_FILE)"; \
		$(TOUCH) $(CACHE_FILE); \
	else \
		echo "Error in PDF generation. Check $(LATEX_DIR)/$(PROJECT).log"; \
		exit 1; \
	fi

# Cleanup
clean:
	@echo "Cleaning $(PROJECT)..."
	$(RM) $(LATEX_DIR)/$(PROJECT).{aux,log,out,toc,pdf}
	$(RM) $(LATEX_DIR)/gs-adonis.cls
	$(RM) $(PDF_OUTPUT)/$(PROJECT).pdf
	$(RM) $(CACHE_FILE) $(MD5_FILE)
