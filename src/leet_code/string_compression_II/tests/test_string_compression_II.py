def test_string_compression_II_runtime_compression():
    from string_compression_II.solution_1 import runtime_compression

    assert "a5b3cd2" == runtime_compression("aaaaabbbcdd")
