"""
Data schema definitions for the 2x2 Factorial LLM Code-First Testing Experiment.
"""

from dataclasses import dataclass, field, asdict
from typing import Optional, List, Dict, Any
from enum import Enum


class ExperimentalCondition(str, Enum):
    T0_SPEC_SAME = "T0_Spec_Same"      # Spec-only, same model as coder
    T1_CODE_SAME = "T1_Code_Same"      # Spec + Faulty Code, same model (Intra-Model)
    T2_CODE_CROSS = "T2_Code_Cross"    # Spec + Faulty Code, cross-family model
    T3_SPEC_CROSS = "T3_Spec_Cross"    # Spec-only, cross-family model


@dataclass
class ProblemSpec:
    problem_id: str
    function_name: str
    docstring: str
    signature: str
    ref_implementation: str
    ref_test: str
    repo_url: str = ""
    commit_hash: str = ""
    commit_date: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class CoderOutput:
    problem_id: str
    model_name: str
    candidate_code: str
    is_faulty: bool
    ref_test_output: str
    error_type: Optional[str] = None  # e.g., AssertionError, IndexError, etc.
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class TestOracleOutput:
    problem_id: str
    condition: ExperimentalCondition
    model_name: str
    generated_test: str
    is_valid: bool                 # Passed on C_ref
    detects_fault: bool            # Failed on C_faulty (valid tests only)
    validation_output: str = ""    # Raw stdout/stderr on C_ref
    detection_output: str = ""     # Raw stdout/stderr on C_faulty
    execution_time_ms: float = 0.0
    prompt_tokens: int = 0
    completion_tokens: int = 0
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d['condition'] = self.condition.value
        return d
