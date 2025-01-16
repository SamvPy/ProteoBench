from __future__ import annotations

import pandas as pd
from pandas import DataFrame

from proteobench.datapoint.quant_datapoint import Datapoint
from proteobench.exceptions import (
    ConvertStandardFormatError,
    DatapointAppendError,
    DatapointGenerationError,
    IntermediateFormatGenerationError,
    ParseError,
    ParseSettingsError,
    QuantificationError,
)
from proteobench.io.parsing.parse_ion import load_input_file
from proteobench.io.parsing.parse_settings_ion import ParseSettingsBuilder
from proteobench.modules.dia_quant_ion.dia_quant_ion_module import DIAQuantIonModule
from proteobench.score.quant.quantscores import QuantScores


class DIAQuantIonModuleSC(DIAQuantIonModule):
    """DIA Quantification Module for Ion level Quantification for single-cell dataset."""
    
    def __init__(
        self,
        token: str,
        proteobot_repo_name: str = "Proteobot/Results_quant_ion_DIA_singlecell",
        proteobench_repo_name: str = "Proteobench/Results_quant_ion_DIA_singlecell",
    ):
        """
        DIA Quantification Module for Ion level Quantification.

        Parameters
        ----------
        token
            GitHub token for the user.
        proteobot_repo_name
            Name of the repository for pull requests and where new points are added.
        proteobench_repo_name
            Name of the repository where the benchmarking results will be stored.

        Attributes
        ----------
        precursor_name: str
            Level of quantification.

        """
        super().__init__(token, proteobot_repo_name=proteobot_repo_name, proteobench_repo_name=proteobench_repo_name)
        self.precursor_name = "precursor ion"