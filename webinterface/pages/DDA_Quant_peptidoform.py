import logging
from typing import Any, Dict, Type

import pages.texts.proteobench_builder as pbb
import streamlit as st
from pages.base_pages.quant import QuantUIObjects
from pages.pages_variables.dda_quant_peptidoform_variables import VariablesDDAQuant
from pages.texts.generic_texts import WebpageTexts

from proteobench.io.parsing.parse_settings_peptidoform import ParseSettingsBuilder
from proteobench.modules.dda_quant_peptidoform.dda_quant_peptidoform_module import DDAQuantPeptidoformModule


class StreamlitUI:
    def __init__(self):
        self.variables_dda_quant: VariablesDDAQuant = VariablesDDAQuant()
        self.texts: Type[WebpageTexts] = WebpageTexts
        self.texts.ShortMessages.title = "DDA peptidoform quantification"

        self.user_input: Dict[str, Any] = dict()

        pbb.proteobench_page_config()

        if self.variables_dda_quant.submit not in st.session_state:
            st.session_state[self.variables_dda_quant.submit] = False
        try:
            token = st.secrets["gh"]["token"]
        except KeyError:
            token = ""

        self.peptidoform_module: DDAQuantPeptidoformModule = DDAQuantPeptidoformModule(token=token)
        self.parsesettingsbuilder = ParseSettingsBuilder()

        self.quant_uiobjects = QuantUIObjects(
            self.variables_dda_quant, self.peptidoform_module, self.parsesettingsbuilder
        )

        self._main_page()

    def _main_page(self) -> None:
        """
        Sets up the main page layout for the Streamlit application.
        This includes the title, module descriptions, input forms, and configuration settings.
        """
        self.quant_uiobjects.create_text_header()
        self.quant_uiobjects.create_main_submission_form()
        self.quant_uiobjects.init_slider()

        if self.quant_uiobjects.variables_quant.fig_logfc in st.session_state:
            self.quant_uiobjects.populate_results()

        self.quant_uiobjects.create_results()


if __name__ == "__main__":
    logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)
    StreamlitUI()  # Instantiate and run the extended UI class
