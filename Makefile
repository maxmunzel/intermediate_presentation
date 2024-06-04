presentation.pdf: presentation.tex space.tex presentation.blg scatter.tex Interpretation.pdf ex1.tex ex2.tex ex3.tex ../thesis/table_improvement_ratios_5.tex ../thesis/table_improvement_ratios_5_triangle.tex ex4_table.tex
	pdflatex presentation.tex
	chktex presentation.tex

Interpretation.pdf: Interpretation.dot
	dot Interpretation.dot -T pdf -o Interpretation.pdf

presentation.blg: presentation.bib
	pdflatex presentation.tex
	biber presentation

