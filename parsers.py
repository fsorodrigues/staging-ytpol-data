# local modules (parsers)
import parser_functions.fig1 as fig1
import parser_functions.fig2 as fig2
import parser_functions.fig3 as fig3
import parser_functions.fig4 as fig4
import parser_functions.fig5 as fig5

steps = {
  'youtube-paper/updated plots/all_1K/fig1_pnas_mean.csv': fig1.parse,
  'youtube-paper/updated plots/all_7K/fig2A_ledwich.csv': fig2.parseA,
  'youtube-paper/updated plots/all_7K/fig2B_ledwich.csv': fig2.parseB,
  'youtube-paper/updated plots/all_7K/fig3A_ledwich.csv': fig3.parseA,
  'youtube-paper/updated plots/all_7K/fig3B_ledwich.csv': fig3.parseB,
  'youtube-paper/outdated plots/Fig4_transition_matrix.txt': fig4.parse,
  'youtube-paper/outdated plots/Fig5.txt': fig5.parse,
}