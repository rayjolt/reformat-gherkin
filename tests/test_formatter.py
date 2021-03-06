from reformat_gherkin.ast_node import GherkinDocument
from reformat_gherkin.formatter import LineGenerator
from reformat_gherkin.options import AlignmentMode


def format_ast(ast, alignment_mode=AlignmentMode.LEFT):
    line_generator = LineGenerator(ast, alignment_mode)
    lines = line_generator.generate()
    return "\n".join(lines)


def test_format_empty_ast():
    assert format_ast(GherkinDocument(())) == ""
