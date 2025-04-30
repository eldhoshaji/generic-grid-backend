table_config = [
    { 
        "table_name": "users",
        "column_configs": [
            {
                "title": "Name",
                "key": "name",
                "type": "string",
                "filterable": False,
                "sortable": True,
                "searchable": True
            },
            {
                "title": "Age",
                "key": "age",
                "type": "heatmap",
                "filterable": False,
                "sortable": True,
                "searchable": False
            },
            {
                "title": "Address",
                "key": "address",
                "type": "string",
                "filterable": True,
                "sortable": False,
                "searchable": False
            },
            {
                "title": "Tags",
                "key": "tags",
                "type": "tags",
                "filterable": False,
                "sortable": False,
                "searchable": False
            }
        ],
        "row_style_rules": [
            {
                "field": 'age',
                "operator": 'gt',
                "value": 50,
                "class_name": 'bg-red-50',
            },
            {
                "field": 'age',
                "operator": 'lt',
                "value": 50,
                "class_name": 'bg-green-50',
            }
        ]
    },
    {
        "table_name": "products",
        "column_configs": [
            {
                "title": "Product ID",
                "key": "id",
                "type": "string",
                "filterable": False,
                "sortable": True,
                "searchable": False
            },
            {
                "title": "Product Name",
                "key": "name",
                "type": "string",
                "filterable": False,
                "sortable": True,
                "searchable": True
            },
            {
                "title": "Price",
                "key": "price",
                "type": "currency",
                "filterable": False,
                "sortable": False,
                "searchable": True
            },
            {
                "title": "Description",
                "key": "description",
                "type": "string",
                "filterable": False,
                "sortable": False,
                "searchable": True
            },
            {
                "title": "Purchase Date",
                "key": "purchase_date",
                "type": "date",
                "filterable": False,
                "sortable": True,
                "searchable": False
            },
            {
                "title": "Product Link",
                "key": "product_link",
                "type": "link",
                "filterable": False,
                "sortable": False,
                "searchable": True
            },
            {
                "title": "Category",
                "key": "category",
                "type": "tags",
                "filterable": False,
                "sortable": False,
                "searchable": True
            }
            
        ],
        "row_style_rules": [
            {
                "field": "purchase_date",
                "operator": "lt",
                "value": "2025-01-01",
                "class_name": "bg-red-50"
            }
        ]
    },
    {
        "table_name": "product_price_comparison",
        "column_configs": [
            # {
            #     "title": "Product ID",
            #     "key": "id",
            #     "type": "number",
            #     "filterable": False,
            #     "sortable": True,
            #     "searchable": False
            # },
            {
                "title": "Product Name",
                "key": "name",
                "type": "number",
                "filterable": False,
                "sortable": True,
                "searchable": True
            },
            {
                "title": "2015",
                "key": "price_2015",
                "type": "heatmap",
                "filterable": False,
                "sortable": True,
                "searchable": False
            },
            {
                "title": "2016",
                "key": "price_2016",
                "type": "heatmap",
                "filterable": False,
                "sortable": True,
                "searchable": False
            },
            {
                "title": "2017",
                "key": "price_2017",
                "type": "heatmap",
                "filterable": False,
                "sortable": True,
                "searchable": False
            },
            {
                "title": "2018",
                "key": "price_2018",
                "type": "heatmap",
                "filterable": False,
                "sortable": True,
                "searchable": False
            },
            {
                "title": "2019",
                "key": "price_2019",
                "type": "heatmap",
                "filterable": False,
                "sortable": True,
                "searchable": False
            },
            {
                "title": "2020",
                "key": "price_2020",
                "type": "heatmap",
                "filterable": False,
                "sortable": True,
                "searchable": False
            },
            {
                "title": "2021",
                "key": "price_2021",
                "type": "heatmap",
                "filterable": False,
                "sortable": True,
                "searchable": False
            },
            {
                "title": "2022",
                "key": "price_2022",
                "type": "heatmap",
                "filterable": False,
                "sortable": True,
                "searchable": False
            },
            {
                "title": "2023",
                "key": "price_2023",
                "type": "heatmap",
                "filterable": False,
                "sortable": True,
                "searchable": False
            },
            {
                "title": "2024",
                "key": "price_2024",
                "type": "heatmap",
                "filterable": False,
                "sortable": True,
                "searchable": False
            },
            {
                "title": "2025",
                "key": "price_2025",
                "type": "heatmap",
                "filterable": False,
                "sortable": True,
                "searchable": False
            }
        ],
        "row_style_rules": []
    }
]
