from pydantic import BaseModel
from typing import Any, Literal, List


class FilterOption(BaseModel):
    text: str
    value: str


class RowStyleRules(BaseModel):
    field: str
    operator: Literal[
        'equals', 'notEquals', 'lt', 'gt', 'lte', 'gte',
        'includes', 'startsWith', 'endsWith', 'matches'
    ]
    value: Any
    class_name: str


class ColumnConfig(BaseModel):
    key: str
    title: str
    type: str
    filterable: bool
    sortable: bool
    searchable: bool
    filters: List[FilterOption] = []


class TableConfigResponseModel(BaseModel):
    table_name: str
    row_style_rules: List[RowStyleRules]
    column_configs: List[ColumnConfig]
