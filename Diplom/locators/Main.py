class Main:
    """
    Locators of the elements that are located on the 'Settings' page.
    """

    class Login:
        login_button = {"class": "login-btn"}
        username = {"id":"login-email"}
        password = {"id":"login-password"}
        further = {"id":"login-btn"}

    class Text_check:
        start_text = {"xpath": "//h4[contains(text(), 'Здравствуйте!')]"}
        learning_button = {"xpath": "//span[contains(text(), 'Проектное обучение')]"}
        text_learning = {"xpath": "//h1[contains(text(), 'Здравствуйте, Константин')]"}
        events_button = {"xpath": "//span[contains(text(), 'Мероприятия')]"}
        text_events = {"xpath": "//h1[contains(text(), 'Мероприятия')]"}

        statements = {"xpath": "//span[contains(text(), 'Реестр организаций')]"}
        text_statements = {"xpath": "//h3[contains(text(), 'Реестр организаций')]"}

        ymnoc = {"xpath": "//span[contains(text(), 'УМНОЦ')]"}
        text_ymnoc = {"xpath": "//h1[contains(text(), 'Ввод и модерация данных')]"}

    class Create_project:
        project_button = {"xpath": "//span[contains(text(), 'Проекты')]"}
        project_create = {"xpath": "//button[contains(text(), ' Создать новый проект ')]"}
        # project_create = {"class": "btn btn-primary"}
        name_project = {"xpath": "//body[1]/div[2]/main[1]/div[1]/div[1]/div[4]/div[1]/div[1]"
                                 "/div[3]/div[1]/fieldset[1]/div[1]/textarea[1]"}
        time_start = {"xpath": "//body/div[2]/main[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[4]"
                               "/div[1]/fieldset[1]/div[1]/span[1]/div[1]/input[1]"}
        time_end = {"xpath": "//body/div[2]/main[1]/div[1]/div[1]/div[4]/div[1]/div[1]"
                             "/div[4]/div[2]/fieldset[1]/div[1]/span[1]/div[1]/input[1]"}

        for_scroll = {"xpath":"//body[1]/div[2]/main[1]/div[1]/div[1]/div[4]"
                              "/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]"}
        type = {"xpath": "//body[1]/div[2]/main[1]/div[1]/div[1]/div[4]/div[1]/div[1]"
                         "/div[5]/div[1]/fieldset[1]/div[1]/div[1]/div[1]"}
        type_choice = {"xpath": "//span[contains(text(), 'Технологический проект (перспективный)')]"}
        line_business = {"xpath": "//body[1]/div[2]/main[1]/div[1]/div[1]/div[4]/div[1]/div[1]"
                                  "/div[6]/div[1]/fieldset[1]/div[1]/div[1]"}
        line_choice = {"xpath": "//span[contains(text(), 'Аэрокосмос')]"}
        second_click = {"xpath":"//body[1]/div[2]/main[1]/div[1]/div[1]/div[4]/"
                                "div[1]/div[1]/div[6]/div[1]/fieldset[1]/div[1]/div[1]/div[1]"}
        subject = {"xpath": "//body[1]/div[2]/main[1]/div[1]/div[1]/div[4]/div[1]/"
                            "div[1]/div[7]/div[1]/fieldset[1]/div[1]/div[1]/div[1]"}
        subject_choice = {"xpath": "//span[contains(text(), 'Свердловская область')]"}

        conformity = {"xpath":"//body[1]/div[2]/main[1]/div[1]/div[1]/div[4]/div[1]/"
                              "div[1]/div[8]/div[1]/div[1]/div[2]/div[1]/fieldset[1]/div[1]/div[1]/div[1]"}
        conformity_choice = {"xpath":"//span[contains(text(), 'деятельность профессиональная, научная и техническая')]"}
        npa = {"xpath":"//body[1]/div[2]/main[1]/div[1]/div[1]/div[4]/div[1]/div[1]/"
                       "div[8]/div[1]/div[1]/div[2]/div[2]/fieldset[1]/div[1]/input[1]"}
        conformity_2 = {"xpath":"//body[1]/div[2]/main[1]/div[1]/div[1]/div[4]/div[1]/"
                                "div[1]/div[9]/div[1]/div[1]/div[2]/div[1]/fieldset[1]/div[1]/div[1]/div[1]"}
        conformity_2_choice = {"xpath":"//span[contains(text(), 'Стратегия промышленного и инновационного развития "
                                       "Свердловской области на период до 2035 года')]"}

        tag_scroll = {"xpath":"//body[1]/div[2]/main[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[9]/div[1]/div[1]"}
        tags = {"xpath": "//body[1]/div[2]/main[1]/div[1]/div[1]/div[4]/div[1]/div[1]"
                         "/div[12]/div[1]/fieldset[1]/div[1]/textarea[1]"}

        novelty = {"xpath":"//body[1]/div[2]/main[1]/div[1]/div[1]/div[4]/"
                           "div[2]/div[1]/div[2]/div[1]/fieldset[1]/div[1]/textarea[1]"}
        problems = {"xpath":"//body[1]/div[2]/main[1]/div[1]/div[1]/div[4]/div[2]/"
                            "div[1]/div[3]/div[1]/fieldset[1]/div[1]/textarea[1]"}
        purpose = {"xpath":"//body[1]/div[2]/main[1]/div[1]/div[1]/div[4]/div[2]/"
                           "div[1]/div[4]/div[1]/fieldset[1]/div[1]/textarea[1]"}
        tasks = {"xpath":"//body[1]/div[2]/main[1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[5]/"
                         "div[1]/fieldset[1]/div[1]/div[1]/div[2]/div[1]/textarea[1]"}
        stage = {"xpath":"//label[contains(text(), 'Инициация ')]"}
        description = {"xpath":"//body[1]/div[2]/main[1]/div[1]/div[1]/div[4]/div[2]/"
                               "div[1]/div[6]/div[1]/fieldset[1]/div[1]/textarea[1]"}
        effects = {"xpath":"//body[1]/div[2]/main[1]/div[1]/div[1]/div[4]/div[2]/div[1]/"
                           "div[7]/div[1]/fieldset[1]/div[1]/textarea[1]"}
        results = {"xpath":"//body[1]/div[2]/main[1]/div[1]/div[1]/div[4]/div[3]/div[1]/"
                           "div[2]/div[1]/fieldset[1]/div[1]/textarea[1]"}
        milestone = {"xpath":"//body[1]/div[2]/main[1]/div[1]/div[1]/div[4]/div[3]/div[1]/"
                             "div[3]/div[1]/fieldset[1]/div[1]/div[1]/div[2]/div[1]/fieldset[1]/div[1]/input[1]"}
        month = {"xpath":"//body[1]/div[2]/main[1]/div[1]/div[1]/div[4]/div[3]/div[1]/div[3]/"
                         "div[1]/fieldset[1]/div[1]/div[1]/div[2]/div[2]/fieldset[1]/div[1]/div[1]/div[2]/input[1]"}
        january = {"xpath":"/html[1]/body[1]/div[2]/main[1]/div[1]/div[1]/div[4]/div[3]/div[1]/div[3]/div[1]/"
                           "fieldset[1]/div[1]/div[1]/div[2]/div[2]/fieldset[1]/div[1]/div[1]/div[2]/span[1]"}
        year = {"xpath":"//body[1]/div[2]/main[1]/div[1]/div[1]/div[4]/div[3]/div[1]/div[3]/div[1]/"
                        "fieldset[1]/div[1]/div[1]/div[2]/div[3]/fieldset[1]/div[1]/div[1]/div[2]/input[1]"}
        choice_year = {"xpath":"//body[1]/div[2]/main[1]/div[1]/div[1]/div[4]/div[3]/div[1]/div[3]/div[1]/fieldset[1]/"
                               "div[1]/div[1]/div[2]/div[3]/fieldset[1]/div[1]/div[1]/div[3]/ul[1]/li[1]/span[1]"}
        type_milestone = {"xpath":"//body[1]/div[2]/main[1]/div[1]/div[1]/div[4]/div[3]/div[1]/div[3]/div[1]/fieldset"
                                  "[1]/div[1]/div[1]/div[2]/div[4]/fieldset[1]/div[1]/div[1]/div[1]/label[1]"}
        perspectives = {"xpath":"//body[1]/div[2]/main[1]/div[1]/div[1]/div[4]/div[3]/div[1]/"
                                "div[13]/div[1]/fieldset[1]/div[1]/textarea[1]"}
        name_organization = {"xpath":"//body[1]/div[2]/main[1]/div[1]/div[1]/div[4]/div[5]/div[1]/div[2]/div[1]/"
                                     "fieldset[1]/div[1]/div[1]/div[2]/div[1]/fieldset[1]/div[1]/div[1]/div[2]/input[1]"}
        acvarium = {"xpath":"//body[1]/div[2]/main[1]/div[1]/div[1]/div[4]/div[5]/div[1]/div[2]/div[1]/fieldset[1]/"
                            "div[1]/div[1]/div[2]/div[1]/fieldset[1]/div[1]/div[1]/div[2]"}
        description_role = {"xpath":"//body[1]/div[2]/main[1]/div[1]/div[1]/div[4]/div[5]/div[1]/div[2]/div[1]/fieldset"
                                    "[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/fieldset[1]/div[1]/input[1]"}
        perspectives_scroll = {"xpath":"//body[1]/div[2]/main[1]/div[1]/div[1]/div[4]/div[3]/div[1]/"
                                       "div[10]/div[1]/fieldset[1]/legend[1]/label[1]/div[1]/span[1]"}
        novelty_scroll = {"xpath":"//body[1]/div[2]/main[1]/div[1]/div[1]/div[4]/div[1]/"
                                  "div[1]/div[11]/div[1]/fieldset[1]/legend[1]/label[1]/span[1]"}
        tasks_scroll = {"xpath":"//body[1]/div[2]/main[1]/div[1]/div[1]/div[4]/div[3]/div[1]/div[1]/div[1]/div[1]/span[1]}"}
        results_scroll = {"xpath":"//body[1]/div[2]/main[1]/div[1]/div[1]/div[4]/div[2]/"
                                  "div[1]/div[7]/div[1]/fieldset[1]/legend[1]/label[1]/span[1]"}
        name_organization_scroll = {"xpath":"//body[1]/div[2]/main[1]/div[1]/div[1]/div[4]/div[4]/div[1]"
                                            "/div[8]/div[1]/fieldset[1]/legend[1]/label[1]/span[1]"}

    class Project_report:
        open_report = {"xpath":"//body[1]/div[2]/main[1]/div[1]/div[1]/div[62]/div[1]/div[1]/div[2]/div[1]/h1[1]/a[1]"}
        report_scroll = {"xpath":"//body[1]/div[2]/main[1]/div[1]/div[1]/div[61]/div[1]/div[1]/div[2]/div[1]/h1[1]/a[1]"}
        editing_button = {"xpath":"//button[contains(text(), 'Редактировать ')]"}
        current_results = {"xpath":"//span[contains(text(), 'Добавить незапланированный результат')]"}
        name_milestone = {"xpath":"//body[1]/div[2]/main[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]/"
                                  "fieldset[1]/div[1]/div[1]/div[2]/div[1]/fieldset[1]/div[1]/input[1]"}
        scroll = {"xpath":"//body[1]/div[2]/main[1]/div[1]/div[1]/div[3]/div[1]/"
                          "div[1]/div[1]/div[1]/div[1]/div[1]/span[1]"}
        month = {"xpath":"//body[1]/div[2]/main[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]/fieldset[1]/"
                         "div[1]/div[1]/div[4]/div[3]/fieldset[1]/div[1]/div[1]/div[2]/input[1]"}
        january = {"xpath":"//body[1]/div[2]/main[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]/fieldset[1]/"
                           "div[1]/div[1]/div[4]/div[3]/fieldset[1]/div[1]/div[1]/div[3]/ul[1]/li[1]/span[1]"}
        year = {"xpath":"//body[1]/div[2]/main[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]/fieldset[1]/"
                        "div[1]/div[1]/div[4]/div[4]/fieldset[1]/div[1]/div[1]/div[2]/input[1]"}
        year_choice = {"xpath":"//body[1]/div[2]/main[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]/fieldset[1]"
                               "/div[1]/div[1]/div[4]/div[4]/fieldset[1]/div[1]/div[1]/div[3]/ul[1]/li[1]/span[1]"}
        description = {"xpath":"//body[1]/div[2]/main[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]/fieldset[1]/"
                               "div[1]/div[1]/div[5]/div[1]/fieldset[1]/div[1]/textarea[1]"}

