import time
from datetime import datetime

from locators import Main
from page_objects import BasePage


class MainPage(BasePage):
    """
    Activities during which testing is carried out.
    """

    def login(self):
        self._click(Main.Login.login_button)
        self._input_text('sklyar.kostya17@gmail.com', Main.Login.username)
        self._click(Main.Login.further)
        self._input_text('k8f!KpLd8K', Main.Login.password)
        self._click(Main.Login.further)
        return MainPage(self.driver)

    def page_switching(self):
        # self._check_if_element_is_visible(Main.Text_check.start_text)
        # self._click(Main.Text_check.statements)
        # self._check_if_element_is_visible(Main.Text_check.text_statements)

        # self._click(Main.Text_check.learning_button)
        # self._click(Main.Text_check.learning_button)
        # self._check_if_element_is_visible(Main.Text_check.text_learning)
        #
        # self._click(Main.Text_check.events_button)
        # self._check_if_element_is_visible(Main.Text_check.text_events)
        self._click(Main.Text_check.ymnoc)
        return MainPage(self.driver)

    def create_project(self):
        self._click(Main.Create_project.project_button)
        self._click(Main.Create_project.project_create)
        self._input_text('Тестовый проект Скляр', Main.Create_project.name_project)
        self._input_text('1.04.2022', Main.Create_project.time_start)
        self._input_text('1.04.2023', Main.Create_project.time_end)

        self._scroll_to(Main.Create_project.for_scroll)
        self._click(Main.Create_project.type)
        self._click(Main.Create_project.type_choice)
        self._click(Main.Create_project.line_business)
        self._click(Main.Create_project.line_choice)
        self._click(Main.Create_project.second_click)
        self._click(Main.Create_project.subject)
        self._click(Main.Create_project.subject_choice)
        self._click(Main.Create_project.subject)

        self._click(Main.Create_project.conformity)
        self._click(Main.Create_project.conformity_choice)
        self._input_text('тест', Main.Create_project.npa)
        self._scroll_to(Main.Create_project.tag_scroll)
        self._input_text('ИИ', Main.Create_project.tags)

        self._scroll_to(Main.Create_project.novelty_scroll)
        self._input_text('супер новая', Main.Create_project.novelty)
        self._input_text('проблема', Main.Create_project.problems)
        self._input_text('цель', Main.Create_project.purpose)
        self._scroll_to(Main.Create_project.tasks_scroll)
        self._input_text('задача', Main.Create_project.tasks)
        self._click(Main.Create_project.stage)
        self._input_text('описание', Main.Create_project.description)
        self._input_text('эффекты', Main.Create_project.effects)
        self._scroll_to(Main.Create_project.results_scroll)
        self._input_text('результаты', Main.Create_project.results)
        self._input_text('веха', Main.Create_project.milestone)
        self._click(Main.Create_project.month)
        self._click(Main.Create_project.january)
        self._click(Main.Create_project.year)
        self._click(Main.Create_project.choice_year)
        self._click(Main.Create_project.type_milestone)
        self._scroll_to(Main.Create_project.perspectives_scroll)
        self._input_text('перспективные', Main.Create_project.perspectives)
        self._scroll_to(Main.Create_project.name_organization_scroll)
        self._input_text('акв', Main.Create_project.name_organization)
        self._click(Main.Create_project.acvarium)
        self._input_text('описание', Main.Create_project.description_role)

    def filling_out_report(self):
        self._click(Main.Project_report.report_scroll)
        self._click(Main.Project_report.open_report)
        self._click(Main.Project_report.editing_button)
        self._click(Main.Project_report.current_results)
        self._input_text('веха', Main.Project_report.name_milestone)
        self._click(Main.Project_report.month)
        self._click(Main.Project_report.january)
        self._click(Main.Project_report.year)
        self._click(Main.Project_report.year_choice)
        self._input_text('описание', Main.Project_report.description)



        return MainPage(self.driver)

