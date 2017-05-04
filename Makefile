DIAS = $(wildcard src/images/*.dia)
PNGS = $(patsubst %.dia,%.png,$(DIAS))

all: single

.PHONY: clean html show

src/images/%.png: src/images/%.dia
	dia $< --export=$@ --filter=png-libart

setup: $(PNGS)

html: setup
	sphinx-build -n . _build

single: setup
	sphinx-build -b singlehtml -n . _build_single
	ln -s _build_single/_images

clean:
	rm -rf _build _build_single _images

show:
	xdg-open _build/src/index.html
