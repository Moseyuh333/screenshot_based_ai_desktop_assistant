def build_prompt(extracted_text: str, correction_mode: bool = False) -> str:
    """
    Build the appropriate prompt based on whether correction mode is active.

    :param extracted_text: The text extracted from the screenshot.
    :param correction_mode: Boolean flag for correction mode.
    :return: Formatted prompt string.
    """

    if correction_mode:
        prompt = f"""Correct the OCR text below.
Return only the corrected text. Do not explain your instructions.
Keep the original language.

OCR text:
{extracted_text}"""
    else:
        prompt = f"""Answer the user's OCR text directly.
Do not discuss these instructions.
If the OCR text is Vietnamese, answer in Vietnamese without accents if needed.
Use short bullets for lists and include brief examples when the question asks for examples.

OCR text:
{extracted_text}"""

    return prompt
