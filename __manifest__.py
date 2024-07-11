{
    "name": "Valults Customized Website",
    "author": "Ahmed Eid Abdallah",
    "category": "",
    "version": "17.0.0.1.0",
    "depends": ["base", "website"],
    "data": [
        "views/website_templates/customized_website_layout.xml",
        "views/website_templates/homepage_template.xml",
        "views/website_templates/companypage_template.xml",
    ],
    "assets":{
        "web.assets_frontend":[
            "vaults/static/src/css/frontend/header_style.css",
            "vaults/static/src/css/frontend/footer_style.css",
            "vaults/static/src/css/frontend/homepage_style.css",
            "vaults/static/src/css/frontend/companypage_style.css",
        ]
    },
    "application": True,

}