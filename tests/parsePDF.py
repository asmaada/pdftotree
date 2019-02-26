import pdftotree

#input_pdf_file="input/paleo.pdf"
#output_html_file="output/"
input_pdf_file="SampleDatasets4sharingNew/inputs/T100_Report.pdf"
output_html_file="SampleDatasets4sharingNew/outputs/"

def heuristic_parsing():
    """Simply test that parse runs to completion without errors."""
    output = pdftotree.parse(input_pdf_file, html_path=output_html_file, model_type=None, model_path=None, favor_figures=True, visualize=False)
    return output


def ml_parsing():
    """Simply test that ML-based parse runs without errors."""
    output = pdftotree.parse(input_pdf_file, html_path=output_html_file, model_type="ml", model_path="input/paleo_model.pkl")
    return output


def visual_parsing():
    """Simply test that ML-based parse runs without errors."""
    output = pdftotree.parse(input_pdf_file, html_path=output_html_file, model_type="visual", model_path="input/paleo_visual_model.h5" )
    return output



#pdftotree.parse("input/paleo.pdf", html_path="output", model_type=None, model_path=None, favor_figures=True, visualize=False)

heuristic_parsing()
#ml_parsing()
#visual_parsing()