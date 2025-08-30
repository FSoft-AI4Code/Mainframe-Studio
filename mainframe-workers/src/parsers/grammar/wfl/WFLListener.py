# Generated from grammar/wfl/WFL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .WFLParser import WFLParser
else:
    from WFLParser import WFLParser

# This class defines a complete listener for a parse tree produced by WFLParser.
class WFLListener(ParseTreeListener):

    # Enter a parse tree produced by WFLParser#startRule.
    def enterStartRule(self, ctx:WFLParser.StartRuleContext):
        pass

    # Exit a parse tree produced by WFLParser#startRule.
    def exitStartRule(self, ctx:WFLParser.StartRuleContext):
        pass


    # Enter a parse tree produced by WFLParser#job.
    def enterJob(self, ctx:WFLParser.JobContext):
        pass

    # Exit a parse tree produced by WFLParser#job.
    def exitJob(self, ctx:WFLParser.JobContext):
        pass


    # Enter a parse tree produced by WFLParser#beginJob.
    def enterBeginJob(self, ctx:WFLParser.BeginJobContext):
        pass

    # Exit a parse tree produced by WFLParser#beginJob.
    def exitBeginJob(self, ctx:WFLParser.BeginJobContext):
        pass


    # Enter a parse tree produced by WFLParser#hostname.
    def enterHostname(self, ctx:WFLParser.HostnameContext):
        pass

    # Exit a parse tree produced by WFLParser#hostname.
    def exitHostname(self, ctx:WFLParser.HostnameContext):
        pass


    # Enter a parse tree produced by WFLParser#parameters.
    def enterParameters(self, ctx:WFLParser.ParametersContext):
        pass

    # Exit a parse tree produced by WFLParser#parameters.
    def exitParameters(self, ctx:WFLParser.ParametersContext):
        pass


    # Enter a parse tree produced by WFLParser#parameterList.
    def enterParameterList(self, ctx:WFLParser.ParameterListContext):
        pass

    # Exit a parse tree produced by WFLParser#parameterList.
    def exitParameterList(self, ctx:WFLParser.ParameterListContext):
        pass


    # Enter a parse tree produced by WFLParser#parameter.
    def enterParameter(self, ctx:WFLParser.ParameterContext):
        pass

    # Exit a parse tree produced by WFLParser#parameter.
    def exitParameter(self, ctx:WFLParser.ParameterContext):
        pass


    # Enter a parse tree produced by WFLParser#parameterDefaultValue.
    def enterParameterDefaultValue(self, ctx:WFLParser.ParameterDefaultValueContext):
        pass

    # Exit a parse tree produced by WFLParser#parameterDefaultValue.
    def exitParameterDefaultValue(self, ctx:WFLParser.ParameterDefaultValueContext):
        pass


    # Enter a parse tree produced by WFLParser#dataType.
    def enterDataType(self, ctx:WFLParser.DataTypeContext):
        pass

    # Exit a parse tree produced by WFLParser#dataType.
    def exitDataType(self, ctx:WFLParser.DataTypeContext):
        pass


    # Enter a parse tree produced by WFLParser#endJob.
    def enterEndJob(self, ctx:WFLParser.EndJobContext):
        pass

    # Exit a parse tree produced by WFLParser#endJob.
    def exitEndJob(self, ctx:WFLParser.EndJobContext):
        pass


    # Enter a parse tree produced by WFLParser#filePath.
    def enterFilePath(self, ctx:WFLParser.FilePathContext):
        pass

    # Exit a parse tree produced by WFLParser#filePath.
    def exitFilePath(self, ctx:WFLParser.FilePathContext):
        pass


    # Enter a parse tree produced by WFLParser#equal.
    def enterEqual(self, ctx:WFLParser.EqualContext):
        pass

    # Exit a parse tree produced by WFLParser#equal.
    def exitEqual(self, ctx:WFLParser.EqualContext):
        pass


    # Enter a parse tree produced by WFLParser#filePathName.
    def enterFilePathName(self, ctx:WFLParser.FilePathNameContext):
        pass

    # Exit a parse tree produced by WFLParser#filePathName.
    def exitFilePathName(self, ctx:WFLParser.FilePathNameContext):
        pass


    # Enter a parse tree produced by WFLParser#filePathNameChar.
    def enterFilePathNameChar(self, ctx:WFLParser.FilePathNameCharContext):
        pass

    # Exit a parse tree produced by WFLParser#filePathNameChar.
    def exitFilePathNameChar(self, ctx:WFLParser.FilePathNameCharContext):
        pass


    # Enter a parse tree produced by WFLParser#attributes.
    def enterAttributes(self, ctx:WFLParser.AttributesContext):
        pass

    # Exit a parse tree produced by WFLParser#attributes.
    def exitAttributes(self, ctx:WFLParser.AttributesContext):
        pass


    # Enter a parse tree produced by WFLParser#attribute.
    def enterAttribute(self, ctx:WFLParser.AttributeContext):
        pass

    # Exit a parse tree produced by WFLParser#attribute.
    def exitAttribute(self, ctx:WFLParser.AttributeContext):
        pass


    # Enter a parse tree produced by WFLParser#stackLimitAttribute.
    def enterStackLimitAttribute(self, ctx:WFLParser.StackLimitAttributeContext):
        pass

    # Exit a parse tree produced by WFLParser#stackLimitAttribute.
    def exitStackLimitAttribute(self, ctx:WFLParser.StackLimitAttributeContext):
        pass


    # Enter a parse tree produced by WFLParser#optionsAttribute.
    def enterOptionsAttribute(self, ctx:WFLParser.OptionsAttributeContext):
        pass

    # Exit a parse tree produced by WFLParser#optionsAttribute.
    def exitOptionsAttribute(self, ctx:WFLParser.OptionsAttributeContext):
        pass


    # Enter a parse tree produced by WFLParser#optionList.
    def enterOptionList(self, ctx:WFLParser.OptionListContext):
        pass

    # Exit a parse tree produced by WFLParser#optionList.
    def exitOptionList(self, ctx:WFLParser.OptionListContext):
        pass


    # Enter a parse tree produced by WFLParser#option.
    def enterOption(self, ctx:WFLParser.OptionContext):
        pass

    # Exit a parse tree produced by WFLParser#option.
    def exitOption(self, ctx:WFLParser.OptionContext):
        pass


    # Enter a parse tree produced by WFLParser#languageAttribute.
    def enterLanguageAttribute(self, ctx:WFLParser.LanguageAttributeContext):
        pass

    # Exit a parse tree produced by WFLParser#languageAttribute.
    def exitLanguageAttribute(self, ctx:WFLParser.LanguageAttributeContext):
        pass


    # Enter a parse tree produced by WFLParser#bdNameAttribute.
    def enterBdNameAttribute(self, ctx:WFLParser.BdNameAttributeContext):
        pass

    # Exit a parse tree produced by WFLParser#bdNameAttribute.
    def exitBdNameAttribute(self, ctx:WFLParser.BdNameAttributeContext):
        pass


    # Enter a parse tree produced by WFLParser#startTimeAttribute.
    def enterStartTimeAttribute(self, ctx:WFLParser.StartTimeAttributeContext):
        pass

    # Exit a parse tree produced by WFLParser#startTimeAttribute.
    def exitStartTimeAttribute(self, ctx:WFLParser.StartTimeAttributeContext):
        pass


    # Enter a parse tree produced by WFLParser#startTimeSpec.
    def enterStartTimeSpec(self, ctx:WFLParser.StartTimeSpecContext):
        pass

    # Exit a parse tree produced by WFLParser#startTimeSpec.
    def exitStartTimeSpec(self, ctx:WFLParser.StartTimeSpecContext):
        pass


    # Enter a parse tree produced by WFLParser#time.
    def enterTime(self, ctx:WFLParser.TimeContext):
        pass

    # Exit a parse tree produced by WFLParser#time.
    def exitTime(self, ctx:WFLParser.TimeContext):
        pass


    # Enter a parse tree produced by WFLParser#timeInterval.
    def enterTimeInterval(self, ctx:WFLParser.TimeIntervalContext):
        pass

    # Exit a parse tree produced by WFLParser#timeInterval.
    def exitTimeInterval(self, ctx:WFLParser.TimeIntervalContext):
        pass


    # Enter a parse tree produced by WFLParser#date.
    def enterDate(self, ctx:WFLParser.DateContext):
        pass

    # Exit a parse tree produced by WFLParser#date.
    def exitDate(self, ctx:WFLParser.DateContext):
        pass


    # Enter a parse tree produced by WFLParser#dayOfWeek.
    def enterDayOfWeek(self, ctx:WFLParser.DayOfWeekContext):
        pass

    # Exit a parse tree produced by WFLParser#dayOfWeek.
    def exitDayOfWeek(self, ctx:WFLParser.DayOfWeekContext):
        pass


    # Enter a parse tree produced by WFLParser#month.
    def enterMonth(self, ctx:WFLParser.MonthContext):
        pass

    # Exit a parse tree produced by WFLParser#month.
    def exitMonth(self, ctx:WFLParser.MonthContext):
        pass


    # Enter a parse tree produced by WFLParser#mm.
    def enterMm(self, ctx:WFLParser.MmContext):
        pass

    # Exit a parse tree produced by WFLParser#mm.
    def exitMm(self, ctx:WFLParser.MmContext):
        pass


    # Enter a parse tree produced by WFLParser#dd.
    def enterDd(self, ctx:WFLParser.DdContext):
        pass

    # Exit a parse tree produced by WFLParser#dd.
    def exitDd(self, ctx:WFLParser.DdContext):
        pass


    # Enter a parse tree produced by WFLParser#yy.
    def enterYy(self, ctx:WFLParser.YyContext):
        pass

    # Exit a parse tree produced by WFLParser#yy.
    def exitYy(self, ctx:WFLParser.YyContext):
        pass


    # Enter a parse tree produced by WFLParser#yyyy.
    def enterYyyy(self, ctx:WFLParser.YyyyContext):
        pass

    # Exit a parse tree produced by WFLParser#yyyy.
    def exitYyyy(self, ctx:WFLParser.YyyyContext):
        pass


    # Enter a parse tree produced by WFLParser#yyddd.
    def enterYyddd(self, ctx:WFLParser.YydddContext):
        pass

    # Exit a parse tree produced by WFLParser#yyddd.
    def exitYyddd(self, ctx:WFLParser.YydddContext):
        pass


    # Enter a parse tree produced by WFLParser#yyyyddd.
    def enterYyyyddd(self, ctx:WFLParser.YyyydddContext):
        pass

    # Exit a parse tree produced by WFLParser#yyyyddd.
    def exitYyyyddd(self, ctx:WFLParser.YyyydddContext):
        pass


    # Enter a parse tree produced by WFLParser#dayInterval.
    def enterDayInterval(self, ctx:WFLParser.DayIntervalContext):
        pass

    # Exit a parse tree produced by WFLParser#dayInterval.
    def exitDayInterval(self, ctx:WFLParser.DayIntervalContext):
        pass


    # Enter a parse tree produced by WFLParser#fetchAttribute.
    def enterFetchAttribute(self, ctx:WFLParser.FetchAttributeContext):
        pass

    # Exit a parse tree produced by WFLParser#fetchAttribute.
    def exitFetchAttribute(self, ctx:WFLParser.FetchAttributeContext):
        pass


    # Enter a parse tree produced by WFLParser#maxIOTimeAttribute.
    def enterMaxIOTimeAttribute(self, ctx:WFLParser.MaxIOTimeAttributeContext):
        pass

    # Exit a parse tree produced by WFLParser#maxIOTimeAttribute.
    def exitMaxIOTimeAttribute(self, ctx:WFLParser.MaxIOTimeAttributeContext):
        pass


    # Enter a parse tree produced by WFLParser#maxLinesAttribute.
    def enterMaxLinesAttribute(self, ctx:WFLParser.MaxLinesAttributeContext):
        pass

    # Exit a parse tree produced by WFLParser#maxLinesAttribute.
    def exitMaxLinesAttribute(self, ctx:WFLParser.MaxLinesAttributeContext):
        pass


    # Enter a parse tree produced by WFLParser#maxProcTimeAttribute.
    def enterMaxProcTimeAttribute(self, ctx:WFLParser.MaxProcTimeAttributeContext):
        pass

    # Exit a parse tree produced by WFLParser#maxProcTimeAttribute.
    def exitMaxProcTimeAttribute(self, ctx:WFLParser.MaxProcTimeAttributeContext):
        pass


    # Enter a parse tree produced by WFLParser#maxWaitAttribute.
    def enterMaxWaitAttribute(self, ctx:WFLParser.MaxWaitAttributeContext):
        pass

    # Exit a parse tree produced by WFLParser#maxWaitAttribute.
    def exitMaxWaitAttribute(self, ctx:WFLParser.MaxWaitAttributeContext):
        pass


    # Enter a parse tree produced by WFLParser#elapsedLimitAttribute.
    def enterElapsedLimitAttribute(self, ctx:WFLParser.ElapsedLimitAttributeContext):
        pass

    # Exit a parse tree produced by WFLParser#elapsedLimitAttribute.
    def exitElapsedLimitAttribute(self, ctx:WFLParser.ElapsedLimitAttributeContext):
        pass


    # Enter a parse tree produced by WFLParser#familyAttribute.
    def enterFamilyAttribute(self, ctx:WFLParser.FamilyAttributeContext):
        pass

    # Exit a parse tree produced by WFLParser#familyAttribute.
    def exitFamilyAttribute(self, ctx:WFLParser.FamilyAttributeContext):
        pass


    # Enter a parse tree produced by WFLParser#reservedKeyword.
    def enterReservedKeyword(self, ctx:WFLParser.ReservedKeywordContext):
        pass

    # Exit a parse tree produced by WFLParser#reservedKeyword.
    def exitReservedKeyword(self, ctx:WFLParser.ReservedKeywordContext):
        pass


    # Enter a parse tree produced by WFLParser#accessCodeAttribute.
    def enterAccessCodeAttribute(self, ctx:WFLParser.AccessCodeAttributeContext):
        pass

    # Exit a parse tree produced by WFLParser#accessCodeAttribute.
    def exitAccessCodeAttribute(self, ctx:WFLParser.AccessCodeAttributeContext):
        pass


    # Enter a parse tree produced by WFLParser#userAttribute.
    def enterUserAttribute(self, ctx:WFLParser.UserAttributeContext):
        pass

    # Exit a parse tree produced by WFLParser#userAttribute.
    def exitUserAttribute(self, ctx:WFLParser.UserAttributeContext):
        pass


    # Enter a parse tree produced by WFLParser#userCodeAttribute.
    def enterUserCodeAttribute(self, ctx:WFLParser.UserCodeAttributeContext):
        pass

    # Exit a parse tree produced by WFLParser#userCodeAttribute.
    def exitUserCodeAttribute(self, ctx:WFLParser.UserCodeAttributeContext):
        pass


    # Enter a parse tree produced by WFLParser#classAttribute.
    def enterClassAttribute(self, ctx:WFLParser.ClassAttributeContext):
        pass

    # Exit a parse tree produced by WFLParser#classAttribute.
    def exitClassAttribute(self, ctx:WFLParser.ClassAttributeContext):
        pass


    # Enter a parse tree produced by WFLParser#priorityAttribute.
    def enterPriorityAttribute(self, ctx:WFLParser.PriorityAttributeContext):
        pass

    # Exit a parse tree produced by WFLParser#priorityAttribute.
    def exitPriorityAttribute(self, ctx:WFLParser.PriorityAttributeContext):
        pass


    # Enter a parse tree produced by WFLParser#chargeCodeAttribute.
    def enterChargeCodeAttribute(self, ctx:WFLParser.ChargeCodeAttributeContext):
        pass

    # Exit a parse tree produced by WFLParser#chargeCodeAttribute.
    def exitChargeCodeAttribute(self, ctx:WFLParser.ChargeCodeAttributeContext):
        pass


    # Enter a parse tree produced by WFLParser#declarations.
    def enterDeclarations(self, ctx:WFLParser.DeclarationsContext):
        pass

    # Exit a parse tree produced by WFLParser#declarations.
    def exitDeclarations(self, ctx:WFLParser.DeclarationsContext):
        pass


    # Enter a parse tree produced by WFLParser#declaration.
    def enterDeclaration(self, ctx:WFLParser.DeclarationContext):
        pass

    # Exit a parse tree produced by WFLParser#declaration.
    def exitDeclaration(self, ctx:WFLParser.DeclarationContext):
        pass


    # Enter a parse tree produced by WFLParser#dataDeclaration.
    def enterDataDeclaration(self, ctx:WFLParser.DataDeclarationContext):
        pass

    # Exit a parse tree produced by WFLParser#dataDeclaration.
    def exitDataDeclaration(self, ctx:WFLParser.DataDeclarationContext):
        pass


    # Enter a parse tree produced by WFLParser#dataFilePathDelaration.
    def enterDataFilePathDelaration(self, ctx:WFLParser.DataFilePathDelarationContext):
        pass

    # Exit a parse tree produced by WFLParser#dataFilePathDelaration.
    def exitDataFilePathDelaration(self, ctx:WFLParser.DataFilePathDelarationContext):
        pass


    # Enter a parse tree produced by WFLParser#dataShowName.
    def enterDataShowName(self, ctx:WFLParser.DataShowNameContext):
        pass

    # Exit a parse tree produced by WFLParser#dataShowName.
    def exitDataShowName(self, ctx:WFLParser.DataShowNameContext):
        pass


    # Enter a parse tree produced by WFLParser#dataSystemClause.
    def enterDataSystemClause(self, ctx:WFLParser.DataSystemClauseContext):
        pass

    # Exit a parse tree produced by WFLParser#dataSystemClause.
    def exitDataSystemClause(self, ctx:WFLParser.DataSystemClauseContext):
        pass


    # Enter a parse tree produced by WFLParser#dataSpecification.
    def enterDataSpecification(self, ctx:WFLParser.DataSpecificationContext):
        pass

    # Exit a parse tree produced by WFLParser#dataSpecification.
    def exitDataSpecification(self, ctx:WFLParser.DataSpecificationContext):
        pass


    # Enter a parse tree produced by WFLParser#dataSpecificationAssignment.
    def enterDataSpecificationAssignment(self, ctx:WFLParser.DataSpecificationAssignmentContext):
        pass

    # Exit a parse tree produced by WFLParser#dataSpecificationAssignment.
    def exitDataSpecificationAssignment(self, ctx:WFLParser.DataSpecificationAssignmentContext):
        pass


    # Enter a parse tree produced by WFLParser#dataSpecificationSection.
    def enterDataSpecificationSection(self, ctx:WFLParser.DataSpecificationSectionContext):
        pass

    # Exit a parse tree produced by WFLParser#dataSpecificationSection.
    def exitDataSpecificationSection(self, ctx:WFLParser.DataSpecificationSectionContext):
        pass


    # Enter a parse tree produced by WFLParser#dataSpecificationEntry.
    def enterDataSpecificationEntry(self, ctx:WFLParser.DataSpecificationEntryContext):
        pass

    # Exit a parse tree produced by WFLParser#dataSpecificationEntry.
    def exitDataSpecificationEntry(self, ctx:WFLParser.DataSpecificationEntryContext):
        pass


    # Enter a parse tree produced by WFLParser#dataSpecificationSectionType.
    def enterDataSpecificationSectionType(self, ctx:WFLParser.DataSpecificationSectionTypeContext):
        pass

    # Exit a parse tree produced by WFLParser#dataSpecificationSectionType.
    def exitDataSpecificationSectionType(self, ctx:WFLParser.DataSpecificationSectionTypeContext):
        pass


    # Enter a parse tree produced by WFLParser#dataSpecificationSectionName.
    def enterDataSpecificationSectionName(self, ctx:WFLParser.DataSpecificationSectionNameContext):
        pass

    # Exit a parse tree produced by WFLParser#dataSpecificationSectionName.
    def exitDataSpecificationSectionName(self, ctx:WFLParser.DataSpecificationSectionNameContext):
        pass


    # Enter a parse tree produced by WFLParser#dataSpecificationAttribute.
    def enterDataSpecificationAttribute(self, ctx:WFLParser.DataSpecificationAttributeContext):
        pass

    # Exit a parse tree produced by WFLParser#dataSpecificationAttribute.
    def exitDataSpecificationAttribute(self, ctx:WFLParser.DataSpecificationAttributeContext):
        pass


    # Enter a parse tree produced by WFLParser#dataSpecificationValue.
    def enterDataSpecificationValue(self, ctx:WFLParser.DataSpecificationValueContext):
        pass

    # Exit a parse tree produced by WFLParser#dataSpecificationValue.
    def exitDataSpecificationValue(self, ctx:WFLParser.DataSpecificationValueContext):
        pass


    # Enter a parse tree produced by WFLParser#dataUseClause.
    def enterDataUseClause(self, ctx:WFLParser.DataUseClauseContext):
        pass

    # Exit a parse tree produced by WFLParser#dataUseClause.
    def exitDataUseClause(self, ctx:WFLParser.DataUseClauseContext):
        pass


    # Enter a parse tree produced by WFLParser#dataUseClauseComponent.
    def enterDataUseClauseComponent(self, ctx:WFLParser.DataUseClauseComponentContext):
        pass

    # Exit a parse tree produced by WFLParser#dataUseClauseComponent.
    def exitDataUseClauseComponent(self, ctx:WFLParser.DataUseClauseComponentContext):
        pass


    # Enter a parse tree produced by WFLParser#headingComponent.
    def enterHeadingComponent(self, ctx:WFLParser.HeadingComponentContext):
        pass

    # Exit a parse tree produced by WFLParser#headingComponent.
    def exitHeadingComponent(self, ctx:WFLParser.HeadingComponentContext):
        pass


    # Enter a parse tree produced by WFLParser#pageComponent.
    def enterPageComponent(self, ctx:WFLParser.PageComponentContext):
        pass

    # Exit a parse tree produced by WFLParser#pageComponent.
    def exitPageComponent(self, ctx:WFLParser.PageComponentContext):
        pass


    # Enter a parse tree produced by WFLParser#includeComponent.
    def enterIncludeComponent(self, ctx:WFLParser.IncludeComponentContext):
        pass

    # Exit a parse tree produced by WFLParser#includeComponent.
    def exitIncludeComponent(self, ctx:WFLParser.IncludeComponentContext):
        pass


    # Enter a parse tree produced by WFLParser#excludeComponent.
    def enterExcludeComponent(self, ctx:WFLParser.ExcludeComponentContext):
        pass

    # Exit a parse tree produced by WFLParser#excludeComponent.
    def exitExcludeComponent(self, ctx:WFLParser.ExcludeComponentContext):
        pass


    # Enter a parse tree produced by WFLParser#outputComponent.
    def enterOutputComponent(self, ctx:WFLParser.OutputComponentContext):
        pass

    # Exit a parse tree produced by WFLParser#outputComponent.
    def exitOutputComponent(self, ctx:WFLParser.OutputComponentContext):
        pass


    # Enter a parse tree produced by WFLParser#reportsComponent.
    def enterReportsComponent(self, ctx:WFLParser.ReportsComponentContext):
        pass

    # Exit a parse tree produced by WFLParser#reportsComponent.
    def exitReportsComponent(self, ctx:WFLParser.ReportsComponentContext):
        pass


    # Enter a parse tree produced by WFLParser#outputItems.
    def enterOutputItems(self, ctx:WFLParser.OutputItemsContext):
        pass

    # Exit a parse tree produced by WFLParser#outputItems.
    def exitOutputItems(self, ctx:WFLParser.OutputItemsContext):
        pass


    # Enter a parse tree produced by WFLParser#useComponent.
    def enterUseComponent(self, ctx:WFLParser.UseComponentContext):
        pass

    # Exit a parse tree produced by WFLParser#useComponent.
    def exitUseComponent(self, ctx:WFLParser.UseComponentContext):
        pass


    # Enter a parse tree produced by WFLParser#reportComponent.
    def enterReportComponent(self, ctx:WFLParser.ReportComponentContext):
        pass

    # Exit a parse tree produced by WFLParser#reportComponent.
    def exitReportComponent(self, ctx:WFLParser.ReportComponentContext):
        pass


    # Enter a parse tree produced by WFLParser#sourceComponent.
    def enterSourceComponent(self, ctx:WFLParser.SourceComponentContext):
        pass

    # Exit a parse tree produced by WFLParser#sourceComponent.
    def exitSourceComponent(self, ctx:WFLParser.SourceComponentContext):
        pass


    # Enter a parse tree produced by WFLParser#sortByComponent.
    def enterSortByComponent(self, ctx:WFLParser.SortByComponentContext):
        pass

    # Exit a parse tree produced by WFLParser#sortByComponent.
    def exitSortByComponent(self, ctx:WFLParser.SortByComponentContext):
        pass


    # Enter a parse tree produced by WFLParser#sortByParam.
    def enterSortByParam(self, ctx:WFLParser.SortByParamContext):
        pass

    # Exit a parse tree produced by WFLParser#sortByParam.
    def exitSortByParam(self, ctx:WFLParser.SortByParamContext):
        pass


    # Enter a parse tree produced by WFLParser#breakComponent.
    def enterBreakComponent(self, ctx:WFLParser.BreakComponentContext):
        pass

    # Exit a parse tree produced by WFLParser#breakComponent.
    def exitBreakComponent(self, ctx:WFLParser.BreakComponentContext):
        pass


    # Enter a parse tree produced by WFLParser#breakOnParam.
    def enterBreakOnParam(self, ctx:WFLParser.BreakOnParamContext):
        pass

    # Exit a parse tree produced by WFLParser#breakOnParam.
    def exitBreakOnParam(self, ctx:WFLParser.BreakOnParamContext):
        pass


    # Enter a parse tree produced by WFLParser#totalling.
    def enterTotalling(self, ctx:WFLParser.TotallingContext):
        pass

    # Exit a parse tree produced by WFLParser#totalling.
    def exitTotalling(self, ctx:WFLParser.TotallingContext):
        pass


    # Enter a parse tree produced by WFLParser#totallingParam.
    def enterTotallingParam(self, ctx:WFLParser.TotallingParamContext):
        pass

    # Exit a parse tree produced by WFLParser#totallingParam.
    def exitTotallingParam(self, ctx:WFLParser.TotallingParamContext):
        pass


    # Enter a parse tree produced by WFLParser#databaseClause.
    def enterDatabaseClause(self, ctx:WFLParser.DatabaseClauseContext):
        pass

    # Exit a parse tree produced by WFLParser#databaseClause.
    def exitDatabaseClause(self, ctx:WFLParser.DatabaseClauseContext):
        pass


    # Enter a parse tree produced by WFLParser#databaseMalnipulationOptions.
    def enterDatabaseMalnipulationOptions(self, ctx:WFLParser.DatabaseMalnipulationOptionsContext):
        pass

    # Exit a parse tree produced by WFLParser#databaseMalnipulationOptions.
    def exitDatabaseMalnipulationOptions(self, ctx:WFLParser.DatabaseMalnipulationOptionsContext):
        pass


    # Enter a parse tree produced by WFLParser#otherDatabaseClauseInput.
    def enterOtherDatabaseClauseInput(self, ctx:WFLParser.OtherDatabaseClauseInputContext):
        pass

    # Exit a parse tree produced by WFLParser#otherDatabaseClauseInput.
    def exitOtherDatabaseClauseInput(self, ctx:WFLParser.OtherDatabaseClauseInputContext):
        pass


    # Enter a parse tree produced by WFLParser#datasetClause.
    def enterDatasetClause(self, ctx:WFLParser.DatasetClauseContext):
        pass

    # Exit a parse tree produced by WFLParser#datasetClause.
    def exitDatasetClause(self, ctx:WFLParser.DatasetClauseContext):
        pass


    # Enter a parse tree produced by WFLParser#datasetDbDeclaration.
    def enterDatasetDbDeclaration(self, ctx:WFLParser.DatasetDbDeclarationContext):
        pass

    # Exit a parse tree produced by WFLParser#datasetDbDeclaration.
    def exitDatasetDbDeclaration(self, ctx:WFLParser.DatasetDbDeclarationContext):
        pass


    # Enter a parse tree produced by WFLParser#datasetDatasetDeclaration.
    def enterDatasetDatasetDeclaration(self, ctx:WFLParser.DatasetDatasetDeclarationContext):
        pass

    # Exit a parse tree produced by WFLParser#datasetDatasetDeclaration.
    def exitDatasetDatasetDeclaration(self, ctx:WFLParser.DatasetDatasetDeclarationContext):
        pass


    # Enter a parse tree produced by WFLParser#datasetFileDeclaration.
    def enterDatasetFileDeclaration(self, ctx:WFLParser.DatasetFileDeclarationContext):
        pass

    # Exit a parse tree produced by WFLParser#datasetFileDeclaration.
    def exitDatasetFileDeclaration(self, ctx:WFLParser.DatasetFileDeclarationContext):
        pass


    # Enter a parse tree produced by WFLParser#datasetRecordDeclaration.
    def enterDatasetRecordDeclaration(self, ctx:WFLParser.DatasetRecordDeclarationContext):
        pass

    # Exit a parse tree produced by WFLParser#datasetRecordDeclaration.
    def exitDatasetRecordDeclaration(self, ctx:WFLParser.DatasetRecordDeclarationContext):
        pass


    # Enter a parse tree produced by WFLParser#datasetSourceDeclaration.
    def enterDatasetSourceDeclaration(self, ctx:WFLParser.DatasetSourceDeclarationContext):
        pass

    # Exit a parse tree produced by WFLParser#datasetSourceDeclaration.
    def exitDatasetSourceDeclaration(self, ctx:WFLParser.DatasetSourceDeclarationContext):
        pass


    # Enter a parse tree produced by WFLParser#datasetLoadDeclaration.
    def enterDatasetLoadDeclaration(self, ctx:WFLParser.DatasetLoadDeclarationContext):
        pass

    # Exit a parse tree produced by WFLParser#datasetLoadDeclaration.
    def exitDatasetLoadDeclaration(self, ctx:WFLParser.DatasetLoadDeclarationContext):
        pass


    # Enter a parse tree produced by WFLParser#dataUserAndAccessCodeListClause.
    def enterDataUserAndAccessCodeListClause(self, ctx:WFLParser.DataUserAndAccessCodeListClauseContext):
        pass

    # Exit a parse tree produced by WFLParser#dataUserAndAccessCodeListClause.
    def exitDataUserAndAccessCodeListClause(self, ctx:WFLParser.DataUserAndAccessCodeListClauseContext):
        pass


    # Enter a parse tree produced by WFLParser#setMergeLabelsintable.
    def enterSetMergeLabelsintable(self, ctx:WFLParser.SetMergeLabelsintableContext):
        pass

    # Exit a parse tree produced by WFLParser#setMergeLabelsintable.
    def exitSetMergeLabelsintable(self, ctx:WFLParser.SetMergeLabelsintableContext):
        pass


    # Enter a parse tree produced by WFLParser#setMergeResetList.
    def enterSetMergeResetList(self, ctx:WFLParser.SetMergeResetListContext):
        pass

    # Exit a parse tree produced by WFLParser#setMergeResetList.
    def exitSetMergeResetList(self, ctx:WFLParser.SetMergeResetListContext):
        pass


    # Enter a parse tree produced by WFLParser#updateClause.
    def enterUpdateClause(self, ctx:WFLParser.UpdateClauseContext):
        pass

    # Exit a parse tree produced by WFLParser#updateClause.
    def exitUpdateClause(self, ctx:WFLParser.UpdateClauseContext):
        pass


    # Enter a parse tree produced by WFLParser#resetZipClause.
    def enterResetZipClause(self, ctx:WFLParser.ResetZipClauseContext):
        pass

    # Exit a parse tree produced by WFLParser#resetZipClause.
    def exitResetZipClause(self, ctx:WFLParser.ResetZipClauseContext):
        pass


    # Enter a parse tree produced by WFLParser#globalAndResourseSetting.
    def enterGlobalAndResourseSetting(self, ctx:WFLParser.GlobalAndResourseSettingContext):
        pass

    # Exit a parse tree produced by WFLParser#globalAndResourseSetting.
    def exitGlobalAndResourseSetting(self, ctx:WFLParser.GlobalAndResourseSettingContext):
        pass


    # Enter a parse tree produced by WFLParser#nopostdumpConfig.
    def enterNopostdumpConfig(self, ctx:WFLParser.NopostdumpConfigContext):
        pass

    # Exit a parse tree produced by WFLParser#nopostdumpConfig.
    def exitNopostdumpConfig(self, ctx:WFLParser.NopostdumpConfigContext):
        pass


    # Enter a parse tree produced by WFLParser#globalConfig.
    def enterGlobalConfig(self, ctx:WFLParser.GlobalConfigContext):
        pass

    # Exit a parse tree produced by WFLParser#globalConfig.
    def exitGlobalConfig(self, ctx:WFLParser.GlobalConfigContext):
        pass


    # Enter a parse tree produced by WFLParser#internalFileConfig.
    def enterInternalFileConfig(self, ctx:WFLParser.InternalFileConfigContext):
        pass

    # Exit a parse tree produced by WFLParser#internalFileConfig.
    def exitInternalFileConfig(self, ctx:WFLParser.InternalFileConfigContext):
        pass


    # Enter a parse tree produced by WFLParser#allowedCoreConfig.
    def enterAllowedCoreConfig(self, ctx:WFLParser.AllowedCoreConfigContext):
        pass

    # Exit a parse tree produced by WFLParser#allowedCoreConfig.
    def exitAllowedCoreConfig(self, ctx:WFLParser.AllowedCoreConfigContext):
        pass


    # Enter a parse tree produced by WFLParser#setListZipClause.
    def enterSetListZipClause(self, ctx:WFLParser.SetListZipClauseContext):
        pass

    # Exit a parse tree produced by WFLParser#setListZipClause.
    def exitSetListZipClause(self, ctx:WFLParser.SetListZipClauseContext):
        pass


    # Enter a parse tree produced by WFLParser#setListClause.
    def enterSetListClause(self, ctx:WFLParser.SetListClauseContext):
        pass

    # Exit a parse tree produced by WFLParser#setListClause.
    def exitSetListClause(self, ctx:WFLParser.SetListClauseContext):
        pass


    # Enter a parse tree produced by WFLParser#generateBlock.
    def enterGenerateBlock(self, ctx:WFLParser.GenerateBlockContext):
        pass

    # Exit a parse tree produced by WFLParser#generateBlock.
    def exitGenerateBlock(self, ctx:WFLParser.GenerateBlockContext):
        pass


    # Enter a parse tree produced by WFLParser#generateParameters.
    def enterGenerateParameters(self, ctx:WFLParser.GenerateParametersContext):
        pass

    # Exit a parse tree produced by WFLParser#generateParameters.
    def exitGenerateParameters(self, ctx:WFLParser.GenerateParametersContext):
        pass


    # Enter a parse tree produced by WFLParser#generateNonCopyParameters.
    def enterGenerateNonCopyParameters(self, ctx:WFLParser.GenerateNonCopyParametersContext):
        pass

    # Exit a parse tree produced by WFLParser#generateNonCopyParameters.
    def exitGenerateNonCopyParameters(self, ctx:WFLParser.GenerateNonCopyParametersContext):
        pass


    # Enter a parse tree produced by WFLParser#generateNonCopyParameter.
    def enterGenerateNonCopyParameter(self, ctx:WFLParser.GenerateNonCopyParameterContext):
        pass

    # Exit a parse tree produced by WFLParser#generateNonCopyParameter.
    def exitGenerateNonCopyParameter(self, ctx:WFLParser.GenerateNonCopyParameterContext):
        pass


    # Enter a parse tree produced by WFLParser#generateCopyParameters.
    def enterGenerateCopyParameters(self, ctx:WFLParser.GenerateCopyParametersContext):
        pass

    # Exit a parse tree produced by WFLParser#generateCopyParameters.
    def exitGenerateCopyParameters(self, ctx:WFLParser.GenerateCopyParametersContext):
        pass


    # Enter a parse tree produced by WFLParser#generateCopyParameter.
    def enterGenerateCopyParameter(self, ctx:WFLParser.GenerateCopyParameterContext):
        pass

    # Exit a parse tree produced by WFLParser#generateCopyParameter.
    def exitGenerateCopyParameter(self, ctx:WFLParser.GenerateCopyParameterContext):
        pass


    # Enter a parse tree produced by WFLParser#orderByClause.
    def enterOrderByClause(self, ctx:WFLParser.OrderByClauseContext):
        pass

    # Exit a parse tree produced by WFLParser#orderByClause.
    def exitOrderByClause(self, ctx:WFLParser.OrderByClauseContext):
        pass


    # Enter a parse tree produced by WFLParser#databaseDeclaration.
    def enterDatabaseDeclaration(self, ctx:WFLParser.DatabaseDeclarationContext):
        pass

    # Exit a parse tree produced by WFLParser#databaseDeclaration.
    def exitDatabaseDeclaration(self, ctx:WFLParser.DatabaseDeclarationContext):
        pass


    # Enter a parse tree produced by WFLParser#databaseOptions.
    def enterDatabaseOptions(self, ctx:WFLParser.DatabaseOptionsContext):
        pass

    # Exit a parse tree produced by WFLParser#databaseOptions.
    def exitDatabaseOptions(self, ctx:WFLParser.DatabaseOptionsContext):
        pass


    # Enter a parse tree produced by WFLParser#databaseOption.
    def enterDatabaseOption(self, ctx:WFLParser.DatabaseOptionContext):
        pass

    # Exit a parse tree produced by WFLParser#databaseOption.
    def exitDatabaseOption(self, ctx:WFLParser.DatabaseOptionContext):
        pass


    # Enter a parse tree produced by WFLParser#dumpDeclaration.
    def enterDumpDeclaration(self, ctx:WFLParser.DumpDeclarationContext):
        pass

    # Exit a parse tree produced by WFLParser#dumpDeclaration.
    def exitDumpDeclaration(self, ctx:WFLParser.DumpDeclarationContext):
        pass


    # Enter a parse tree produced by WFLParser#dumpParameters.
    def enterDumpParameters(self, ctx:WFLParser.DumpParametersContext):
        pass

    # Exit a parse tree produced by WFLParser#dumpParameters.
    def exitDumpParameters(self, ctx:WFLParser.DumpParametersContext):
        pass


    # Enter a parse tree produced by WFLParser#dumpParameter.
    def enterDumpParameter(self, ctx:WFLParser.DumpParameterContext):
        pass

    # Exit a parse tree produced by WFLParser#dumpParameter.
    def exitDumpParameter(self, ctx:WFLParser.DumpParameterContext):
        pass


    # Enter a parse tree produced by WFLParser#includeDeclaration.
    def enterIncludeDeclaration(self, ctx:WFLParser.IncludeDeclarationContext):
        pass

    # Exit a parse tree produced by WFLParser#includeDeclaration.
    def exitIncludeDeclaration(self, ctx:WFLParser.IncludeDeclarationContext):
        pass


    # Enter a parse tree produced by WFLParser#taskDeclaration.
    def enterTaskDeclaration(self, ctx:WFLParser.TaskDeclarationContext):
        pass

    # Exit a parse tree produced by WFLParser#taskDeclaration.
    def exitTaskDeclaration(self, ctx:WFLParser.TaskDeclarationContext):
        pass


    # Enter a parse tree produced by WFLParser#taskIdentifierDeclaration.
    def enterTaskIdentifierDeclaration(self, ctx:WFLParser.TaskIdentifierDeclarationContext):
        pass

    # Exit a parse tree produced by WFLParser#taskIdentifierDeclaration.
    def exitTaskIdentifierDeclaration(self, ctx:WFLParser.TaskIdentifierDeclarationContext):
        pass


    # Enter a parse tree produced by WFLParser#myselfTaskAssignment.
    def enterMyselfTaskAssignment(self, ctx:WFLParser.MyselfTaskAssignmentContext):
        pass

    # Exit a parse tree produced by WFLParser#myselfTaskAssignment.
    def exitMyselfTaskAssignment(self, ctx:WFLParser.MyselfTaskAssignmentContext):
        pass


    # Enter a parse tree produced by WFLParser#myjobTaskAssignment.
    def enterMyjobTaskAssignment(self, ctx:WFLParser.MyjobTaskAssignmentContext):
        pass

    # Exit a parse tree produced by WFLParser#myjobTaskAssignment.
    def exitMyjobTaskAssignment(self, ctx:WFLParser.MyjobTaskAssignmentContext):
        pass


    # Enter a parse tree produced by WFLParser#taskIdentifier.
    def enterTaskIdentifier(self, ctx:WFLParser.TaskIdentifierContext):
        pass

    # Exit a parse tree produced by WFLParser#taskIdentifier.
    def exitTaskIdentifier(self, ctx:WFLParser.TaskIdentifierContext):
        pass


    # Enter a parse tree produced by WFLParser#taskIdentifierAssigments.
    def enterTaskIdentifierAssigments(self, ctx:WFLParser.TaskIdentifierAssigmentsContext):
        pass

    # Exit a parse tree produced by WFLParser#taskIdentifierAssigments.
    def exitTaskIdentifierAssigments(self, ctx:WFLParser.TaskIdentifierAssigmentsContext):
        pass


    # Enter a parse tree produced by WFLParser#taskIdentifierAssigment.
    def enterTaskIdentifierAssigment(self, ctx:WFLParser.TaskIdentifierAssigmentContext):
        pass

    # Exit a parse tree produced by WFLParser#taskIdentifierAssigment.
    def exitTaskIdentifierAssigment(self, ctx:WFLParser.TaskIdentifierAssigmentContext):
        pass


    # Enter a parse tree produced by WFLParser#fileEquation.
    def enterFileEquation(self, ctx:WFLParser.FileEquationContext):
        pass

    # Exit a parse tree produced by WFLParser#fileEquation.
    def exitFileEquation(self, ctx:WFLParser.FileEquationContext):
        pass


    # Enter a parse tree produced by WFLParser#fileAttributeAssignment.
    def enterFileAttributeAssignment(self, ctx:WFLParser.FileAttributeAssignmentContext):
        pass

    # Exit a parse tree produced by WFLParser#fileAttributeAssignment.
    def exitFileAttributeAssignment(self, ctx:WFLParser.FileAttributeAssignmentContext):
        pass


    # Enter a parse tree produced by WFLParser#fileAttribute.
    def enterFileAttribute(self, ctx:WFLParser.FileAttributeContext):
        pass

    # Exit a parse tree produced by WFLParser#fileAttribute.
    def exitFileAttribute(self, ctx:WFLParser.FileAttributeContext):
        pass


    # Enter a parse tree produced by WFLParser#booleanFileAttribute.
    def enterBooleanFileAttribute(self, ctx:WFLParser.BooleanFileAttributeContext):
        pass

    # Exit a parse tree produced by WFLParser#booleanFileAttribute.
    def exitBooleanFileAttribute(self, ctx:WFLParser.BooleanFileAttributeContext):
        pass


    # Enter a parse tree produced by WFLParser#integerFileAttribute.
    def enterIntegerFileAttribute(self, ctx:WFLParser.IntegerFileAttributeContext):
        pass

    # Exit a parse tree produced by WFLParser#integerFileAttribute.
    def exitIntegerFileAttribute(self, ctx:WFLParser.IntegerFileAttributeContext):
        pass


    # Enter a parse tree produced by WFLParser#stringFileAttribute.
    def enterStringFileAttribute(self, ctx:WFLParser.StringFileAttributeContext):
        pass

    # Exit a parse tree produced by WFLParser#stringFileAttribute.
    def exitStringFileAttribute(self, ctx:WFLParser.StringFileAttributeContext):
        pass


    # Enter a parse tree produced by WFLParser#titleFileAttribute.
    def enterTitleFileAttribute(self, ctx:WFLParser.TitleFileAttributeContext):
        pass

    # Exit a parse tree produced by WFLParser#titleFileAttribute.
    def exitTitleFileAttribute(self, ctx:WFLParser.TitleFileAttributeContext):
        pass


    # Enter a parse tree produced by WFLParser#blockSizeFileAttribute.
    def enterBlockSizeFileAttribute(self, ctx:WFLParser.BlockSizeFileAttributeContext):
        pass

    # Exit a parse tree produced by WFLParser#blockSizeFileAttribute.
    def exitBlockSizeFileAttribute(self, ctx:WFLParser.BlockSizeFileAttributeContext):
        pass


    # Enter a parse tree produced by WFLParser#fileNameFileAttribute.
    def enterFileNameFileAttribute(self, ctx:WFLParser.FileNameFileAttributeContext):
        pass

    # Exit a parse tree produced by WFLParser#fileNameFileAttribute.
    def exitFileNameFileAttribute(self, ctx:WFLParser.FileNameFileAttributeContext):
        pass


    # Enter a parse tree produced by WFLParser#longFileNameFileAttribute.
    def enterLongFileNameFileAttribute(self, ctx:WFLParser.LongFileNameFileAttributeContext):
        pass

    # Exit a parse tree produced by WFLParser#longFileNameFileAttribute.
    def exitLongFileNameFileAttribute(self, ctx:WFLParser.LongFileNameFileAttributeContext):
        pass


    # Enter a parse tree produced by WFLParser#longTitleFileAttribute.
    def enterLongTitleFileAttribute(self, ctx:WFLParser.LongTitleFileAttributeContext):
        pass

    # Exit a parse tree produced by WFLParser#longTitleFileAttribute.
    def exitLongTitleFileAttribute(self, ctx:WFLParser.LongTitleFileAttributeContext):
        pass


    # Enter a parse tree produced by WFLParser#mnemonicFileAttribute.
    def enterMnemonicFileAttribute(self, ctx:WFLParser.MnemonicFileAttributeContext):
        pass

    # Exit a parse tree produced by WFLParser#mnemonicFileAttribute.
    def exitMnemonicFileAttribute(self, ctx:WFLParser.MnemonicFileAttributeContext):
        pass


    # Enter a parse tree produced by WFLParser#deviceKindAssigment.
    def enterDeviceKindAssigment(self, ctx:WFLParser.DeviceKindAssigmentContext):
        pass

    # Exit a parse tree produced by WFLParser#deviceKindAssigment.
    def exitDeviceKindAssigment(self, ctx:WFLParser.DeviceKindAssigmentContext):
        pass


    # Enter a parse tree produced by WFLParser#serialNumberAssigment.
    def enterSerialNumberAssigment(self, ctx:WFLParser.SerialNumberAssigmentContext):
        pass

    # Exit a parse tree produced by WFLParser#serialNumberAssigment.
    def exitSerialNumberAssigment(self, ctx:WFLParser.SerialNumberAssigmentContext):
        pass


    # Enter a parse tree produced by WFLParser#fileAttributeValue.
    def enterFileAttributeValue(self, ctx:WFLParser.FileAttributeValueContext):
        pass

    # Exit a parse tree produced by WFLParser#fileAttributeValue.
    def exitFileAttributeValue(self, ctx:WFLParser.FileAttributeValueContext):
        pass


    # Enter a parse tree produced by WFLParser#taskAttributeAssignment.
    def enterTaskAttributeAssignment(self, ctx:WFLParser.TaskAttributeAssignmentContext):
        pass

    # Exit a parse tree produced by WFLParser#taskAttributeAssignment.
    def exitTaskAttributeAssignment(self, ctx:WFLParser.TaskAttributeAssignmentContext):
        pass


    # Enter a parse tree produced by WFLParser#taskAttribute.
    def enterTaskAttribute(self, ctx:WFLParser.TaskAttributeContext):
        pass

    # Exit a parse tree produced by WFLParser#taskAttribute.
    def exitTaskAttribute(self, ctx:WFLParser.TaskAttributeContext):
        pass


    # Enter a parse tree produced by WFLParser#taskAttributeValue.
    def enterTaskAttributeValue(self, ctx:WFLParser.TaskAttributeValueContext):
        pass

    # Exit a parse tree produced by WFLParser#taskAttributeValue.
    def exitTaskAttributeValue(self, ctx:WFLParser.TaskAttributeValueContext):
        pass


    # Enter a parse tree produced by WFLParser#fileDeclaration.
    def enterFileDeclaration(self, ctx:WFLParser.FileDeclarationContext):
        pass

    # Exit a parse tree produced by WFLParser#fileDeclaration.
    def exitFileDeclaration(self, ctx:WFLParser.FileDeclarationContext):
        pass


    # Enter a parse tree produced by WFLParser#fileDeclarationElement.
    def enterFileDeclarationElement(self, ctx:WFLParser.FileDeclarationElementContext):
        pass

    # Exit a parse tree produced by WFLParser#fileDeclarationElement.
    def exitFileDeclarationElement(self, ctx:WFLParser.FileDeclarationElementContext):
        pass


    # Enter a parse tree produced by WFLParser#booleanDeclaration.
    def enterBooleanDeclaration(self, ctx:WFLParser.BooleanDeclarationContext):
        pass

    # Exit a parse tree produced by WFLParser#booleanDeclaration.
    def exitBooleanDeclaration(self, ctx:WFLParser.BooleanDeclarationContext):
        pass


    # Enter a parse tree produced by WFLParser#booleanDeclarationElement.
    def enterBooleanDeclarationElement(self, ctx:WFLParser.BooleanDeclarationElementContext):
        pass

    # Exit a parse tree produced by WFLParser#booleanDeclarationElement.
    def exitBooleanDeclarationElement(self, ctx:WFLParser.BooleanDeclarationElementContext):
        pass


    # Enter a parse tree produced by WFLParser#booleanConstantExpression.
    def enterBooleanConstantExpression(self, ctx:WFLParser.BooleanConstantExpressionContext):
        pass

    # Exit a parse tree produced by WFLParser#booleanConstantExpression.
    def exitBooleanConstantExpression(self, ctx:WFLParser.BooleanConstantExpressionContext):
        pass


    # Enter a parse tree produced by WFLParser#integerDeclaration.
    def enterIntegerDeclaration(self, ctx:WFLParser.IntegerDeclarationContext):
        pass

    # Exit a parse tree produced by WFLParser#integerDeclaration.
    def exitIntegerDeclaration(self, ctx:WFLParser.IntegerDeclarationContext):
        pass


    # Enter a parse tree produced by WFLParser#integerDeclarationElement.
    def enterIntegerDeclarationElement(self, ctx:WFLParser.IntegerDeclarationElementContext):
        pass

    # Exit a parse tree produced by WFLParser#integerDeclarationElement.
    def exitIntegerDeclarationElement(self, ctx:WFLParser.IntegerDeclarationElementContext):
        pass


    # Enter a parse tree produced by WFLParser#integerConstantExpression.
    def enterIntegerConstantExpression(self, ctx:WFLParser.IntegerConstantExpressionContext):
        pass

    # Exit a parse tree produced by WFLParser#integerConstantExpression.
    def exitIntegerConstantExpression(self, ctx:WFLParser.IntegerConstantExpressionContext):
        pass


    # Enter a parse tree produced by WFLParser#realDeclaration.
    def enterRealDeclaration(self, ctx:WFLParser.RealDeclarationContext):
        pass

    # Exit a parse tree produced by WFLParser#realDeclaration.
    def exitRealDeclaration(self, ctx:WFLParser.RealDeclarationContext):
        pass


    # Enter a parse tree produced by WFLParser#realDeclarationElement.
    def enterRealDeclarationElement(self, ctx:WFLParser.RealDeclarationElementContext):
        pass

    # Exit a parse tree produced by WFLParser#realDeclarationElement.
    def exitRealDeclarationElement(self, ctx:WFLParser.RealDeclarationElementContext):
        pass


    # Enter a parse tree produced by WFLParser#realConstantExpression.
    def enterRealConstantExpression(self, ctx:WFLParser.RealConstantExpressionContext):
        pass

    # Exit a parse tree produced by WFLParser#realConstantExpression.
    def exitRealConstantExpression(self, ctx:WFLParser.RealConstantExpressionContext):
        pass


    # Enter a parse tree produced by WFLParser#stringDeclaration.
    def enterStringDeclaration(self, ctx:WFLParser.StringDeclarationContext):
        pass

    # Exit a parse tree produced by WFLParser#stringDeclaration.
    def exitStringDeclaration(self, ctx:WFLParser.StringDeclarationContext):
        pass


    # Enter a parse tree produced by WFLParser#stringDeclarationElement.
    def enterStringDeclarationElement(self, ctx:WFLParser.StringDeclarationElementContext):
        pass

    # Exit a parse tree produced by WFLParser#stringDeclarationElement.
    def exitStringDeclarationElement(self, ctx:WFLParser.StringDeclarationElementContext):
        pass


    # Enter a parse tree produced by WFLParser#stringConstantExpression.
    def enterStringConstantExpression(self, ctx:WFLParser.StringConstantExpressionContext):
        pass

    # Exit a parse tree produced by WFLParser#stringConstantExpression.
    def exitStringConstantExpression(self, ctx:WFLParser.StringConstantExpressionContext):
        pass


    # Enter a parse tree produced by WFLParser#primaryStringExpression.
    def enterPrimaryStringExpression(self, ctx:WFLParser.PrimaryStringExpressionContext):
        pass

    # Exit a parse tree produced by WFLParser#primaryStringExpression.
    def exitPrimaryStringExpression(self, ctx:WFLParser.PrimaryStringExpressionContext):
        pass


    # Enter a parse tree produced by WFLParser#stringFunction.
    def enterStringFunction(self, ctx:WFLParser.StringFunctionContext):
        pass

    # Exit a parse tree produced by WFLParser#stringFunction.
    def exitStringFunction(self, ctx:WFLParser.StringFunctionContext):
        pass


    # Enter a parse tree produced by WFLParser#parameterReference.
    def enterParameterReference(self, ctx:WFLParser.ParameterReferenceContext):
        pass

    # Exit a parse tree produced by WFLParser#parameterReference.
    def exitParameterReference(self, ctx:WFLParser.ParameterReferenceContext):
        pass


    # Enter a parse tree produced by WFLParser#constantDeclaration.
    def enterConstantDeclaration(self, ctx:WFLParser.ConstantDeclarationContext):
        pass

    # Exit a parse tree produced by WFLParser#constantDeclaration.
    def exitConstantDeclaration(self, ctx:WFLParser.ConstantDeclarationContext):
        pass


    # Enter a parse tree produced by WFLParser#constantDeclarationElement.
    def enterConstantDeclarationElement(self, ctx:WFLParser.ConstantDeclarationElementContext):
        pass

    # Exit a parse tree produced by WFLParser#constantDeclarationElement.
    def exitConstantDeclarationElement(self, ctx:WFLParser.ConstantDeclarationElementContext):
        pass


    # Enter a parse tree produced by WFLParser#booleanConstantDeclaration.
    def enterBooleanConstantDeclaration(self, ctx:WFLParser.BooleanConstantDeclarationContext):
        pass

    # Exit a parse tree produced by WFLParser#booleanConstantDeclaration.
    def exitBooleanConstantDeclaration(self, ctx:WFLParser.BooleanConstantDeclarationContext):
        pass


    # Enter a parse tree produced by WFLParser#integerConstantDeclaration.
    def enterIntegerConstantDeclaration(self, ctx:WFLParser.IntegerConstantDeclarationContext):
        pass

    # Exit a parse tree produced by WFLParser#integerConstantDeclaration.
    def exitIntegerConstantDeclaration(self, ctx:WFLParser.IntegerConstantDeclarationContext):
        pass


    # Enter a parse tree produced by WFLParser#realConstantDeclaration.
    def enterRealConstantDeclaration(self, ctx:WFLParser.RealConstantDeclarationContext):
        pass

    # Exit a parse tree produced by WFLParser#realConstantDeclaration.
    def exitRealConstantDeclaration(self, ctx:WFLParser.RealConstantDeclarationContext):
        pass


    # Enter a parse tree produced by WFLParser#stringConstantDeclaration.
    def enterStringConstantDeclaration(self, ctx:WFLParser.StringConstantDeclarationContext):
        pass

    # Exit a parse tree produced by WFLParser#stringConstantDeclaration.
    def exitStringConstantDeclaration(self, ctx:WFLParser.StringConstantDeclarationContext):
        pass


    # Enter a parse tree produced by WFLParser#subroutineDeclaration.
    def enterSubroutineDeclaration(self, ctx:WFLParser.SubroutineDeclarationContext):
        pass

    # Exit a parse tree produced by WFLParser#subroutineDeclaration.
    def exitSubroutineDeclaration(self, ctx:WFLParser.SubroutineDeclarationContext):
        pass


    # Enter a parse tree produced by WFLParser#subroutineName.
    def enterSubroutineName(self, ctx:WFLParser.SubroutineNameContext):
        pass

    # Exit a parse tree produced by WFLParser#subroutineName.
    def exitSubroutineName(self, ctx:WFLParser.SubroutineNameContext):
        pass


    # Enter a parse tree produced by WFLParser#subroutineParameters.
    def enterSubroutineParameters(self, ctx:WFLParser.SubroutineParametersContext):
        pass

    # Exit a parse tree produced by WFLParser#subroutineParameters.
    def exitSubroutineParameters(self, ctx:WFLParser.SubroutineParametersContext):
        pass


    # Enter a parse tree produced by WFLParser#subroutineParameterList.
    def enterSubroutineParameterList(self, ctx:WFLParser.SubroutineParameterListContext):
        pass

    # Exit a parse tree produced by WFLParser#subroutineParameterList.
    def exitSubroutineParameterList(self, ctx:WFLParser.SubroutineParameterListContext):
        pass


    # Enter a parse tree produced by WFLParser#subroutineParameter.
    def enterSubroutineParameter(self, ctx:WFLParser.SubroutineParameterContext):
        pass

    # Exit a parse tree produced by WFLParser#subroutineParameter.
    def exitSubroutineParameter(self, ctx:WFLParser.SubroutineParameterContext):
        pass


    # Enter a parse tree produced by WFLParser#booleanParameter.
    def enterBooleanParameter(self, ctx:WFLParser.BooleanParameterContext):
        pass

    # Exit a parse tree produced by WFLParser#booleanParameter.
    def exitBooleanParameter(self, ctx:WFLParser.BooleanParameterContext):
        pass


    # Enter a parse tree produced by WFLParser#integerParameter.
    def enterIntegerParameter(self, ctx:WFLParser.IntegerParameterContext):
        pass

    # Exit a parse tree produced by WFLParser#integerParameter.
    def exitIntegerParameter(self, ctx:WFLParser.IntegerParameterContext):
        pass


    # Enter a parse tree produced by WFLParser#realParameter.
    def enterRealParameter(self, ctx:WFLParser.RealParameterContext):
        pass

    # Exit a parse tree produced by WFLParser#realParameter.
    def exitRealParameter(self, ctx:WFLParser.RealParameterContext):
        pass


    # Enter a parse tree produced by WFLParser#stringParameter.
    def enterStringParameter(self, ctx:WFLParser.StringParameterContext):
        pass

    # Exit a parse tree produced by WFLParser#stringParameter.
    def exitStringParameter(self, ctx:WFLParser.StringParameterContext):
        pass


    # Enter a parse tree produced by WFLParser#fileParameter.
    def enterFileParameter(self, ctx:WFLParser.FileParameterContext):
        pass

    # Exit a parse tree produced by WFLParser#fileParameter.
    def exitFileParameter(self, ctx:WFLParser.FileParameterContext):
        pass


    # Enter a parse tree produced by WFLParser#taskParameter.
    def enterTaskParameter(self, ctx:WFLParser.TaskParameterContext):
        pass

    # Exit a parse tree produced by WFLParser#taskParameter.
    def exitTaskParameter(self, ctx:WFLParser.TaskParameterContext):
        pass


    # Enter a parse tree produced by WFLParser#subroutineBlock.
    def enterSubroutineBlock(self, ctx:WFLParser.SubroutineBlockContext):
        pass

    # Exit a parse tree produced by WFLParser#subroutineBlock.
    def exitSubroutineBlock(self, ctx:WFLParser.SubroutineBlockContext):
        pass


    # Enter a parse tree produced by WFLParser#fileReferencedVariable.
    def enterFileReferencedVariable(self, ctx:WFLParser.FileReferencedVariableContext):
        pass

    # Exit a parse tree produced by WFLParser#fileReferencedVariable.
    def exitFileReferencedVariable(self, ctx:WFLParser.FileReferencedVariableContext):
        pass


    # Enter a parse tree produced by WFLParser#label.
    def enterLabel(self, ctx:WFLParser.LabelContext):
        pass

    # Exit a parse tree produced by WFLParser#label.
    def exitLabel(self, ctx:WFLParser.LabelContext):
        pass


    # Enter a parse tree produced by WFLParser#statements.
    def enterStatements(self, ctx:WFLParser.StatementsContext):
        pass

    # Exit a parse tree produced by WFLParser#statements.
    def exitStatements(self, ctx:WFLParser.StatementsContext):
        pass


    # Enter a parse tree produced by WFLParser#statement.
    def enterStatement(self, ctx:WFLParser.StatementContext):
        pass

    # Exit a parse tree produced by WFLParser#statement.
    def exitStatement(self, ctx:WFLParser.StatementContext):
        pass


    # Enter a parse tree produced by WFLParser#startAndWaitStatement.
    def enterStartAndWaitStatement(self, ctx:WFLParser.StartAndWaitStatementContext):
        pass

    # Exit a parse tree produced by WFLParser#startAndWaitStatement.
    def exitStartAndWaitStatement(self, ctx:WFLParser.StartAndWaitStatementContext):
        pass


    # Enter a parse tree produced by WFLParser#wrapAndCompressStatement.
    def enterWrapAndCompressStatement(self, ctx:WFLParser.WrapAndCompressStatementContext):
        pass

    # Exit a parse tree produced by WFLParser#wrapAndCompressStatement.
    def exitWrapAndCompressStatement(self, ctx:WFLParser.WrapAndCompressStatementContext):
        pass


    # Enter a parse tree produced by WFLParser#wrapAndCompressFrom.
    def enterWrapAndCompressFrom(self, ctx:WFLParser.WrapAndCompressFromContext):
        pass

    # Exit a parse tree produced by WFLParser#wrapAndCompressFrom.
    def exitWrapAndCompressFrom(self, ctx:WFLParser.WrapAndCompressFromContext):
        pass


    # Enter a parse tree produced by WFLParser#printStatement.
    def enterPrintStatement(self, ctx:WFLParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by WFLParser#printStatement.
    def exitPrintStatement(self, ctx:WFLParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by WFLParser#printSpecification.
    def enterPrintSpecification(self, ctx:WFLParser.PrintSpecificationContext):
        pass

    # Exit a parse tree produced by WFLParser#printSpecification.
    def exitPrintSpecification(self, ctx:WFLParser.PrintSpecificationContext):
        pass


    # Enter a parse tree produced by WFLParser#printDefault.
    def enterPrintDefault(self, ctx:WFLParser.PrintDefaultContext):
        pass

    # Exit a parse tree produced by WFLParser#printDefault.
    def exitPrintDefault(self, ctx:WFLParser.PrintDefaultContext):
        pass


    # Enter a parse tree produced by WFLParser#printDefaultParameters.
    def enterPrintDefaultParameters(self, ctx:WFLParser.PrintDefaultParametersContext):
        pass

    # Exit a parse tree produced by WFLParser#printDefaultParameters.
    def exitPrintDefaultParameters(self, ctx:WFLParser.PrintDefaultParametersContext):
        pass


    # Enter a parse tree produced by WFLParser#printDefaultParameter.
    def enterPrintDefaultParameter(self, ctx:WFLParser.PrintDefaultParameterContext):
        pass

    # Exit a parse tree produced by WFLParser#printDefaultParameter.
    def exitPrintDefaultParameter(self, ctx:WFLParser.PrintDefaultParameterContext):
        pass


    # Enter a parse tree produced by WFLParser#printAttributeValue.
    def enterPrintAttributeValue(self, ctx:WFLParser.PrintAttributeValueContext):
        pass

    # Exit a parse tree produced by WFLParser#printAttributeValue.
    def exitPrintAttributeValue(self, ctx:WFLParser.PrintAttributeValueContext):
        pass


    # Enter a parse tree produced by WFLParser#printAttribute.
    def enterPrintAttribute(self, ctx:WFLParser.PrintAttributeContext):
        pass

    # Exit a parse tree produced by WFLParser#printAttribute.
    def exitPrintAttribute(self, ctx:WFLParser.PrintAttributeContext):
        pass


    # Enter a parse tree produced by WFLParser#copyAndCompareStatement.
    def enterCopyAndCompareStatement(self, ctx:WFLParser.CopyAndCompareStatementContext):
        pass

    # Exit a parse tree produced by WFLParser#copyAndCompareStatement.
    def exitCopyAndCompareStatement(self, ctx:WFLParser.CopyAndCompareStatementContext):
        pass


    # Enter a parse tree produced by WFLParser#copyAndRemoveStatement.
    def enterCopyAndRemoveStatement(self, ctx:WFLParser.CopyAndRemoveStatementContext):
        pass

    # Exit a parse tree produced by WFLParser#copyAndRemoveStatement.
    def exitCopyAndRemoveStatement(self, ctx:WFLParser.CopyAndRemoveStatementContext):
        pass


    # Enter a parse tree produced by WFLParser#copyStatement.
    def enterCopyStatement(self, ctx:WFLParser.CopyStatementContext):
        pass

    # Exit a parse tree produced by WFLParser#copyStatement.
    def exitCopyStatement(self, ctx:WFLParser.CopyStatementContext):
        pass


    # Enter a parse tree produced by WFLParser#copyProtocol.
    def enterCopyProtocol(self, ctx:WFLParser.CopyProtocolContext):
        pass

    # Exit a parse tree produced by WFLParser#copyProtocol.
    def exitCopyProtocol(self, ctx:WFLParser.CopyProtocolContext):
        pass


    # Enter a parse tree produced by WFLParser#copyFromClause.
    def enterCopyFromClause(self, ctx:WFLParser.CopyFromClauseContext):
        pass

    # Exit a parse tree produced by WFLParser#copyFromClause.
    def exitCopyFromClause(self, ctx:WFLParser.CopyFromClauseContext):
        pass


    # Enter a parse tree produced by WFLParser#copyAsClause.
    def enterCopyAsClause(self, ctx:WFLParser.CopyAsClauseContext):
        pass

    # Exit a parse tree produced by WFLParser#copyAsClause.
    def exitCopyAsClause(self, ctx:WFLParser.CopyAsClauseContext):
        pass


    # Enter a parse tree produced by WFLParser#compileStatement.
    def enterCompileStatement(self, ctx:WFLParser.CompileStatementContext):
        pass

    # Exit a parse tree produced by WFLParser#compileStatement.
    def exitCompileStatement(self, ctx:WFLParser.CompileStatementContext):
        pass


    # Enter a parse tree produced by WFLParser#compilerTaskEquationList.
    def enterCompilerTaskEquationList(self, ctx:WFLParser.CompilerTaskEquationListContext):
        pass

    # Exit a parse tree produced by WFLParser#compilerTaskEquationList.
    def exitCompilerTaskEquationList(self, ctx:WFLParser.CompilerTaskEquationListContext):
        pass


    # Enter a parse tree produced by WFLParser#libraryEquation.
    def enterLibraryEquation(self, ctx:WFLParser.LibraryEquationContext):
        pass

    # Exit a parse tree produced by WFLParser#libraryEquation.
    def exitLibraryEquation(self, ctx:WFLParser.LibraryEquationContext):
        pass


    # Enter a parse tree produced by WFLParser#databaseEquation.
    def enterDatabaseEquation(self, ctx:WFLParser.DatabaseEquationContext):
        pass

    # Exit a parse tree produced by WFLParser#databaseEquation.
    def exitDatabaseEquation(self, ctx:WFLParser.DatabaseEquationContext):
        pass


    # Enter a parse tree produced by WFLParser#compilerName.
    def enterCompilerName(self, ctx:WFLParser.CompilerNameContext):
        pass

    # Exit a parse tree produced by WFLParser#compilerName.
    def exitCompilerName(self, ctx:WFLParser.CompilerNameContext):
        pass


    # Enter a parse tree produced by WFLParser#compilerTitle.
    def enterCompilerTitle(self, ctx:WFLParser.CompilerTitleContext):
        pass

    # Exit a parse tree produced by WFLParser#compilerTitle.
    def exitCompilerTitle(self, ctx:WFLParser.CompilerTitleContext):
        pass


    # Enter a parse tree produced by WFLParser#familyName.
    def enterFamilyName(self, ctx:WFLParser.FamilyNameContext):
        pass

    # Exit a parse tree produced by WFLParser#familyName.
    def exitFamilyName(self, ctx:WFLParser.FamilyNameContext):
        pass


    # Enter a parse tree produced by WFLParser#runStatement.
    def enterRunStatement(self, ctx:WFLParser.RunStatementContext):
        pass

    # Exit a parse tree produced by WFLParser#runStatement.
    def exitRunStatement(self, ctx:WFLParser.RunStatementContext):
        pass


    # Enter a parse tree produced by WFLParser#localDataSpecification.
    def enterLocalDataSpecification(self, ctx:WFLParser.LocalDataSpecificationContext):
        pass

    # Exit a parse tree produced by WFLParser#localDataSpecification.
    def exitLocalDataSpecification(self, ctx:WFLParser.LocalDataSpecificationContext):
        pass


    # Enter a parse tree produced by WFLParser#excludeClause.
    def enterExcludeClause(self, ctx:WFLParser.ExcludeClauseContext):
        pass

    # Exit a parse tree produced by WFLParser#excludeClause.
    def exitExcludeClause(self, ctx:WFLParser.ExcludeClauseContext):
        pass


    # Enter a parse tree produced by WFLParser#runParameterList.
    def enterRunParameterList(self, ctx:WFLParser.RunParameterListContext):
        pass

    # Exit a parse tree produced by WFLParser#runParameterList.
    def exitRunParameterList(self, ctx:WFLParser.RunParameterListContext):
        pass


    # Enter a parse tree produced by WFLParser#runParameter.
    def enterRunParameter(self, ctx:WFLParser.RunParameterContext):
        pass

    # Exit a parse tree produced by WFLParser#runParameter.
    def exitRunParameter(self, ctx:WFLParser.RunParameterContext):
        pass


    # Enter a parse tree produced by WFLParser#realExpression.
    def enterRealExpression(self, ctx:WFLParser.RealExpressionContext):
        pass

    # Exit a parse tree produced by WFLParser#realExpression.
    def exitRealExpression(self, ctx:WFLParser.RealExpressionContext):
        pass


    # Enter a parse tree produced by WFLParser#integerExpression.
    def enterIntegerExpression(self, ctx:WFLParser.IntegerExpressionContext):
        pass

    # Exit a parse tree produced by WFLParser#integerExpression.
    def exitIntegerExpression(self, ctx:WFLParser.IntegerExpressionContext):
        pass


    # Enter a parse tree produced by WFLParser#integerMethod.
    def enterIntegerMethod(self, ctx:WFLParser.IntegerMethodContext):
        pass

    # Exit a parse tree produced by WFLParser#integerMethod.
    def exitIntegerMethod(self, ctx:WFLParser.IntegerMethodContext):
        pass


    # Enter a parse tree produced by WFLParser#otherIntegerMethod.
    def enterOtherIntegerMethod(self, ctx:WFLParser.OtherIntegerMethodContext):
        pass

    # Exit a parse tree produced by WFLParser#otherIntegerMethod.
    def exitOtherIntegerMethod(self, ctx:WFLParser.OtherIntegerMethodContext):
        pass


    # Enter a parse tree produced by WFLParser#integerIntegerMethod.
    def enterIntegerIntegerMethod(self, ctx:WFLParser.IntegerIntegerMethodContext):
        pass

    # Exit a parse tree produced by WFLParser#integerIntegerMethod.
    def exitIntegerIntegerMethod(self, ctx:WFLParser.IntegerIntegerMethodContext):
        pass


    # Enter a parse tree produced by WFLParser#calcExpression.
    def enterCalcExpression(self, ctx:WFLParser.CalcExpressionContext):
        pass

    # Exit a parse tree produced by WFLParser#calcExpression.
    def exitCalcExpression(self, ctx:WFLParser.CalcExpressionContext):
        pass


    # Enter a parse tree produced by WFLParser#calcExpressionTerm.
    def enterCalcExpressionTerm(self, ctx:WFLParser.CalcExpressionTermContext):
        pass

    # Exit a parse tree produced by WFLParser#calcExpressionTerm.
    def exitCalcExpressionTerm(self, ctx:WFLParser.CalcExpressionTermContext):
        pass


    # Enter a parse tree produced by WFLParser#calcExpressionFactor.
    def enterCalcExpressionFactor(self, ctx:WFLParser.CalcExpressionFactorContext):
        pass

    # Exit a parse tree produced by WFLParser#calcExpressionFactor.
    def exitCalcExpressionFactor(self, ctx:WFLParser.CalcExpressionFactorContext):
        pass


    # Enter a parse tree produced by WFLParser#stringExpression.
    def enterStringExpression(self, ctx:WFLParser.StringExpressionContext):
        pass

    # Exit a parse tree produced by WFLParser#stringExpression.
    def exitStringExpression(self, ctx:WFLParser.StringExpressionContext):
        pass


    # Enter a parse tree produced by WFLParser#stringMethod.
    def enterStringMethod(self, ctx:WFLParser.StringMethodContext):
        pass

    # Exit a parse tree produced by WFLParser#stringMethod.
    def exitStringMethod(self, ctx:WFLParser.StringMethodContext):
        pass


    # Enter a parse tree produced by WFLParser#otherStringMethod.
    def enterOtherStringMethod(self, ctx:WFLParser.OtherStringMethodContext):
        pass

    # Exit a parse tree produced by WFLParser#otherStringMethod.
    def exitOtherStringMethod(self, ctx:WFLParser.OtherStringMethodContext):
        pass


    # Enter a parse tree produced by WFLParser#acceptMethod.
    def enterAcceptMethod(self, ctx:WFLParser.AcceptMethodContext):
        pass

    # Exit a parse tree produced by WFLParser#acceptMethod.
    def exitAcceptMethod(self, ctx:WFLParser.AcceptMethodContext):
        pass


    # Enter a parse tree produced by WFLParser#timeDateMethod.
    def enterTimeDateMethod(self, ctx:WFLParser.TimeDateMethodContext):
        pass

    # Exit a parse tree produced by WFLParser#timeDateMethod.
    def exitTimeDateMethod(self, ctx:WFLParser.TimeDateMethodContext):
        pass


    # Enter a parse tree produced by WFLParser#timeDateParameter.
    def enterTimeDateParameter(self, ctx:WFLParser.TimeDateParameterContext):
        pass

    # Exit a parse tree produced by WFLParser#timeDateParameter.
    def exitTimeDateParameter(self, ctx:WFLParser.TimeDateParameterContext):
        pass


    # Enter a parse tree produced by WFLParser#myselfMethod.
    def enterMyselfMethod(self, ctx:WFLParser.MyselfMethodContext):
        pass

    # Exit a parse tree produced by WFLParser#myselfMethod.
    def exitMyselfMethod(self, ctx:WFLParser.MyselfMethodContext):
        pass


    # Enter a parse tree produced by WFLParser#myjobMethod.
    def enterMyjobMethod(self, ctx:WFLParser.MyjobMethodContext):
        pass

    # Exit a parse tree produced by WFLParser#myjobMethod.
    def exitMyjobMethod(self, ctx:WFLParser.MyjobMethodContext):
        pass


    # Enter a parse tree produced by WFLParser#takeMethod.
    def enterTakeMethod(self, ctx:WFLParser.TakeMethodContext):
        pass

    # Exit a parse tree produced by WFLParser#takeMethod.
    def exitTakeMethod(self, ctx:WFLParser.TakeMethodContext):
        pass


    # Enter a parse tree produced by WFLParser#dropMethod.
    def enterDropMethod(self, ctx:WFLParser.DropMethodContext):
        pass

    # Exit a parse tree produced by WFLParser#dropMethod.
    def exitDropMethod(self, ctx:WFLParser.DropMethodContext):
        pass


    # Enter a parse tree produced by WFLParser#subStringMethod.
    def enterSubStringMethod(self, ctx:WFLParser.SubStringMethodContext):
        pass

    # Exit a parse tree produced by WFLParser#subStringMethod.
    def exitSubStringMethod(self, ctx:WFLParser.SubStringMethodContext):
        pass


    # Enter a parse tree produced by WFLParser#stringStringMethod.
    def enterStringStringMethod(self, ctx:WFLParser.StringStringMethodContext):
        pass

    # Exit a parse tree produced by WFLParser#stringStringMethod.
    def exitStringStringMethod(self, ctx:WFLParser.StringStringMethodContext):
        pass


    # Enter a parse tree produced by WFLParser#headMethod.
    def enterHeadMethod(self, ctx:WFLParser.HeadMethodContext):
        pass

    # Exit a parse tree produced by WFLParser#headMethod.
    def exitHeadMethod(self, ctx:WFLParser.HeadMethodContext):
        pass


    # Enter a parse tree produced by WFLParser#headParameter.
    def enterHeadParameter(self, ctx:WFLParser.HeadParameterContext):
        pass

    # Exit a parse tree produced by WFLParser#headParameter.
    def exitHeadParameter(self, ctx:WFLParser.HeadParameterContext):
        pass


    # Enter a parse tree produced by WFLParser#tailMethod.
    def enterTailMethod(self, ctx:WFLParser.TailMethodContext):
        pass

    # Exit a parse tree produced by WFLParser#tailMethod.
    def exitTailMethod(self, ctx:WFLParser.TailMethodContext):
        pass


    # Enter a parse tree produced by WFLParser#tailParameter.
    def enterTailParameter(self, ctx:WFLParser.TailParameterContext):
        pass

    # Exit a parse tree produced by WFLParser#tailParameter.
    def exitTailParameter(self, ctx:WFLParser.TailParameterContext):
        pass


    # Enter a parse tree produced by WFLParser#concatMethod.
    def enterConcatMethod(self, ctx:WFLParser.ConcatMethodContext):
        pass

    # Exit a parse tree produced by WFLParser#concatMethod.
    def exitConcatMethod(self, ctx:WFLParser.ConcatMethodContext):
        pass


    # Enter a parse tree produced by WFLParser#taskEquationList.
    def enterTaskEquationList(self, ctx:WFLParser.TaskEquationListContext):
        pass

    # Exit a parse tree produced by WFLParser#taskEquationList.
    def exitTaskEquationList(self, ctx:WFLParser.TaskEquationListContext):
        pass


    # Enter a parse tree produced by WFLParser#displayStatement.
    def enterDisplayStatement(self, ctx:WFLParser.DisplayStatementContext):
        pass

    # Exit a parse tree produced by WFLParser#displayStatement.
    def exitDisplayStatement(self, ctx:WFLParser.DisplayStatementContext):
        pass


    # Enter a parse tree produced by WFLParser#initializeStatement.
    def enterInitializeStatement(self, ctx:WFLParser.InitializeStatementContext):
        pass

    # Exit a parse tree produced by WFLParser#initializeStatement.
    def exitInitializeStatement(self, ctx:WFLParser.InitializeStatementContext):
        pass


    # Enter a parse tree produced by WFLParser#abortStatement.
    def enterAbortStatement(self, ctx:WFLParser.AbortStatementContext):
        pass

    # Exit a parse tree produced by WFLParser#abortStatement.
    def exitAbortStatement(self, ctx:WFLParser.AbortStatementContext):
        pass


    # Enter a parse tree produced by WFLParser#waitStatement.
    def enterWaitStatement(self, ctx:WFLParser.WaitStatementContext):
        pass

    # Exit a parse tree produced by WFLParser#waitStatement.
    def exitWaitStatement(self, ctx:WFLParser.WaitStatementContext):
        pass


    # Enter a parse tree produced by WFLParser#waitContent.
    def enterWaitContent(self, ctx:WFLParser.WaitContentContext):
        pass

    # Exit a parse tree produced by WFLParser#waitContent.
    def exitWaitContent(self, ctx:WFLParser.WaitContentContext):
        pass


    # Enter a parse tree produced by WFLParser#waitSpecification.
    def enterWaitSpecification(self, ctx:WFLParser.WaitSpecificationContext):
        pass

    # Exit a parse tree produced by WFLParser#waitSpecification.
    def exitWaitSpecification(self, ctx:WFLParser.WaitSpecificationContext):
        pass


    # Enter a parse tree produced by WFLParser#simpleTaskRelation.
    def enterSimpleTaskRelation(self, ctx:WFLParser.SimpleTaskRelationContext):
        pass

    # Exit a parse tree produced by WFLParser#simpleTaskRelation.
    def exitSimpleTaskRelation(self, ctx:WFLParser.SimpleTaskRelationContext):
        pass


    # Enter a parse tree produced by WFLParser#taskMnemonicComparison.
    def enterTaskMnemonicComparison(self, ctx:WFLParser.TaskMnemonicComparisonContext):
        pass

    # Exit a parse tree produced by WFLParser#taskMnemonicComparison.
    def exitTaskMnemonicComparison(self, ctx:WFLParser.TaskMnemonicComparisonContext):
        pass


    # Enter a parse tree produced by WFLParser#taskState.
    def enterTaskState(self, ctx:WFLParser.TaskStateContext):
        pass

    # Exit a parse tree produced by WFLParser#taskState.
    def exitTaskState(self, ctx:WFLParser.TaskStateContext):
        pass


    # Enter a parse tree produced by WFLParser#booleanTaskAttribute.
    def enterBooleanTaskAttribute(self, ctx:WFLParser.BooleanTaskAttributeContext):
        pass

    # Exit a parse tree produced by WFLParser#booleanTaskAttribute.
    def exitBooleanTaskAttribute(self, ctx:WFLParser.BooleanTaskAttributeContext):
        pass


    # Enter a parse tree produced by WFLParser#integerTaskAttribute.
    def enterIntegerTaskAttribute(self, ctx:WFLParser.IntegerTaskAttributeContext):
        pass

    # Exit a parse tree produced by WFLParser#integerTaskAttribute.
    def exitIntegerTaskAttribute(self, ctx:WFLParser.IntegerTaskAttributeContext):
        pass


    # Enter a parse tree produced by WFLParser#realTaskAttribute.
    def enterRealTaskAttribute(self, ctx:WFLParser.RealTaskAttributeContext):
        pass

    # Exit a parse tree produced by WFLParser#realTaskAttribute.
    def exitRealTaskAttribute(self, ctx:WFLParser.RealTaskAttributeContext):
        pass


    # Enter a parse tree produced by WFLParser#mnemonicTaskAttribute.
    def enterMnemonicTaskAttribute(self, ctx:WFLParser.MnemonicTaskAttributeContext):
        pass

    # Exit a parse tree produced by WFLParser#mnemonicTaskAttribute.
    def exitMnemonicTaskAttribute(self, ctx:WFLParser.MnemonicTaskAttributeContext):
        pass


    # Enter a parse tree produced by WFLParser#realRelation.
    def enterRealRelation(self, ctx:WFLParser.RealRelationContext):
        pass

    # Exit a parse tree produced by WFLParser#realRelation.
    def exitRealRelation(self, ctx:WFLParser.RealRelationContext):
        pass


    # Enter a parse tree produced by WFLParser#addStatement.
    def enterAddStatement(self, ctx:WFLParser.AddStatementContext):
        pass

    # Exit a parse tree produced by WFLParser#addStatement.
    def exitAddStatement(self, ctx:WFLParser.AddStatementContext):
        pass


    # Enter a parse tree produced by WFLParser#addOptions.
    def enterAddOptions(self, ctx:WFLParser.AddOptionsContext):
        pass

    # Exit a parse tree produced by WFLParser#addOptions.
    def exitAddOptions(self, ctx:WFLParser.AddOptionsContext):
        pass


    # Enter a parse tree produced by WFLParser#addOption.
    def enterAddOption(self, ctx:WFLParser.AddOptionContext):
        pass

    # Exit a parse tree produced by WFLParser#addOption.
    def exitAddOption(self, ctx:WFLParser.AddOptionContext):
        pass


    # Enter a parse tree produced by WFLParser#copyRequest.
    def enterCopyRequest(self, ctx:WFLParser.CopyRequestContext):
        pass

    # Exit a parse tree produced by WFLParser#copyRequest.
    def exitCopyRequest(self, ctx:WFLParser.CopyRequestContext):
        pass


    # Enter a parse tree produced by WFLParser#processStatement.
    def enterProcessStatement(self, ctx:WFLParser.ProcessStatementContext):
        pass

    # Exit a parse tree produced by WFLParser#processStatement.
    def exitProcessStatement(self, ctx:WFLParser.ProcessStatementContext):
        pass


    # Enter a parse tree produced by WFLParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:WFLParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by WFLParser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:WFLParser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by WFLParser#booleanAssignmentStatement.
    def enterBooleanAssignmentStatement(self, ctx:WFLParser.BooleanAssignmentStatementContext):
        pass

    # Exit a parse tree produced by WFLParser#booleanAssignmentStatement.
    def exitBooleanAssignmentStatement(self, ctx:WFLParser.BooleanAssignmentStatementContext):
        pass


    # Enter a parse tree produced by WFLParser#booleanIdentifier.
    def enterBooleanIdentifier(self, ctx:WFLParser.BooleanIdentifierContext):
        pass

    # Exit a parse tree produced by WFLParser#booleanIdentifier.
    def exitBooleanIdentifier(self, ctx:WFLParser.BooleanIdentifierContext):
        pass


    # Enter a parse tree produced by WFLParser#integerAssignmentStatement.
    def enterIntegerAssignmentStatement(self, ctx:WFLParser.IntegerAssignmentStatementContext):
        pass

    # Exit a parse tree produced by WFLParser#integerAssignmentStatement.
    def exitIntegerAssignmentStatement(self, ctx:WFLParser.IntegerAssignmentStatementContext):
        pass


    # Enter a parse tree produced by WFLParser#integerIdentifier.
    def enterIntegerIdentifier(self, ctx:WFLParser.IntegerIdentifierContext):
        pass

    # Exit a parse tree produced by WFLParser#integerIdentifier.
    def exitIntegerIdentifier(self, ctx:WFLParser.IntegerIdentifierContext):
        pass


    # Enter a parse tree produced by WFLParser#realAssignmentStatement.
    def enterRealAssignmentStatement(self, ctx:WFLParser.RealAssignmentStatementContext):
        pass

    # Exit a parse tree produced by WFLParser#realAssignmentStatement.
    def exitRealAssignmentStatement(self, ctx:WFLParser.RealAssignmentStatementContext):
        pass


    # Enter a parse tree produced by WFLParser#realIdentifier.
    def enterRealIdentifier(self, ctx:WFLParser.RealIdentifierContext):
        pass

    # Exit a parse tree produced by WFLParser#realIdentifier.
    def exitRealIdentifier(self, ctx:WFLParser.RealIdentifierContext):
        pass


    # Enter a parse tree produced by WFLParser#stringAssignmentStatement.
    def enterStringAssignmentStatement(self, ctx:WFLParser.StringAssignmentStatementContext):
        pass

    # Exit a parse tree produced by WFLParser#stringAssignmentStatement.
    def exitStringAssignmentStatement(self, ctx:WFLParser.StringAssignmentStatementContext):
        pass


    # Enter a parse tree produced by WFLParser#stringIdentifier.
    def enterStringIdentifier(self, ctx:WFLParser.StringIdentifierContext):
        pass

    # Exit a parse tree produced by WFLParser#stringIdentifier.
    def exitStringIdentifier(self, ctx:WFLParser.StringIdentifierContext):
        pass


    # Enter a parse tree produced by WFLParser#fileAssignmentStatement.
    def enterFileAssignmentStatement(self, ctx:WFLParser.FileAssignmentStatementContext):
        pass

    # Exit a parse tree produced by WFLParser#fileAssignmentStatement.
    def exitFileAssignmentStatement(self, ctx:WFLParser.FileAssignmentStatementContext):
        pass


    # Enter a parse tree produced by WFLParser#fileIdentifier.
    def enterFileIdentifier(self, ctx:WFLParser.FileIdentifierContext):
        pass

    # Exit a parse tree produced by WFLParser#fileIdentifier.
    def exitFileIdentifier(self, ctx:WFLParser.FileIdentifierContext):
        pass


    # Enter a parse tree produced by WFLParser#taskAssignmentStatement.
    def enterTaskAssignmentStatement(self, ctx:WFLParser.TaskAssignmentStatementContext):
        pass

    # Exit a parse tree produced by WFLParser#taskAssignmentStatement.
    def exitTaskAssignmentStatement(self, ctx:WFLParser.TaskAssignmentStatementContext):
        pass


    # Enter a parse tree produced by WFLParser#startStatement.
    def enterStartStatement(self, ctx:WFLParser.StartStatementContext):
        pass

    # Exit a parse tree produced by WFLParser#startStatement.
    def exitStartStatement(self, ctx:WFLParser.StartStatementContext):
        pass


    # Enter a parse tree produced by WFLParser#startParameterList.
    def enterStartParameterList(self, ctx:WFLParser.StartParameterListContext):
        pass

    # Exit a parse tree produced by WFLParser#startParameterList.
    def exitStartParameterList(self, ctx:WFLParser.StartParameterListContext):
        pass


    # Enter a parse tree produced by WFLParser#namedParameterList.
    def enterNamedParameterList(self, ctx:WFLParser.NamedParameterListContext):
        pass

    # Exit a parse tree produced by WFLParser#namedParameterList.
    def exitNamedParameterList(self, ctx:WFLParser.NamedParameterListContext):
        pass


    # Enter a parse tree produced by WFLParser#namedParameter.
    def enterNamedParameter(self, ctx:WFLParser.NamedParameterContext):
        pass

    # Exit a parse tree produced by WFLParser#namedParameter.
    def exitNamedParameter(self, ctx:WFLParser.NamedParameterContext):
        pass


    # Enter a parse tree produced by WFLParser#realFormalParameter.
    def enterRealFormalParameter(self, ctx:WFLParser.RealFormalParameterContext):
        pass

    # Exit a parse tree produced by WFLParser#realFormalParameter.
    def exitRealFormalParameter(self, ctx:WFLParser.RealFormalParameterContext):
        pass


    # Enter a parse tree produced by WFLParser#integerFormalParameter.
    def enterIntegerFormalParameter(self, ctx:WFLParser.IntegerFormalParameterContext):
        pass

    # Exit a parse tree produced by WFLParser#integerFormalParameter.
    def exitIntegerFormalParameter(self, ctx:WFLParser.IntegerFormalParameterContext):
        pass


    # Enter a parse tree produced by WFLParser#booleanFormalParameter.
    def enterBooleanFormalParameter(self, ctx:WFLParser.BooleanFormalParameterContext):
        pass

    # Exit a parse tree produced by WFLParser#booleanFormalParameter.
    def exitBooleanFormalParameter(self, ctx:WFLParser.BooleanFormalParameterContext):
        pass


    # Enter a parse tree produced by WFLParser#stringFormalParameter.
    def enterStringFormalParameter(self, ctx:WFLParser.StringFormalParameterContext):
        pass

    # Exit a parse tree produced by WFLParser#stringFormalParameter.
    def exitStringFormalParameter(self, ctx:WFLParser.StringFormalParameterContext):
        pass


    # Enter a parse tree produced by WFLParser#positionalParameterList.
    def enterPositionalParameterList(self, ctx:WFLParser.PositionalParameterListContext):
        pass

    # Exit a parse tree produced by WFLParser#positionalParameterList.
    def exitPositionalParameterList(self, ctx:WFLParser.PositionalParameterListContext):
        pass


    # Enter a parse tree produced by WFLParser#positionalParameter.
    def enterPositionalParameter(self, ctx:WFLParser.PositionalParameterContext):
        pass

    # Exit a parse tree produced by WFLParser#positionalParameter.
    def exitPositionalParameter(self, ctx:WFLParser.PositionalParameterContext):
        pass


    # Enter a parse tree produced by WFLParser#stringPrimary.
    def enterStringPrimary(self, ctx:WFLParser.StringPrimaryContext):
        pass

    # Exit a parse tree produced by WFLParser#stringPrimary.
    def exitStringPrimary(self, ctx:WFLParser.StringPrimaryContext):
        pass


    # Enter a parse tree produced by WFLParser#ifStatement.
    def enterIfStatement(self, ctx:WFLParser.IfStatementContext):
        pass

    # Exit a parse tree produced by WFLParser#ifStatement.
    def exitIfStatement(self, ctx:WFLParser.IfStatementContext):
        pass


    # Enter a parse tree produced by WFLParser#condition.
    def enterCondition(self, ctx:WFLParser.ConditionContext):
        pass

    # Exit a parse tree produced by WFLParser#condition.
    def exitCondition(self, ctx:WFLParser.ConditionContext):
        pass


    # Enter a parse tree produced by WFLParser#simpleCondition.
    def enterSimpleCondition(self, ctx:WFLParser.SimpleConditionContext):
        pass

    # Exit a parse tree produced by WFLParser#simpleCondition.
    def exitSimpleCondition(self, ctx:WFLParser.SimpleConditionContext):
        pass


    # Enter a parse tree produced by WFLParser#complexCondition.
    def enterComplexCondition(self, ctx:WFLParser.ComplexConditionContext):
        pass

    # Exit a parse tree produced by WFLParser#complexCondition.
    def exitComplexCondition(self, ctx:WFLParser.ComplexConditionContext):
        pass


    # Enter a parse tree produced by WFLParser#combineComplexCondition.
    def enterCombineComplexCondition(self, ctx:WFLParser.CombineComplexConditionContext):
        pass

    # Exit a parse tree produced by WFLParser#combineComplexCondition.
    def exitCombineComplexCondition(self, ctx:WFLParser.CombineComplexConditionContext):
        pass


    # Enter a parse tree produced by WFLParser#thenClause.
    def enterThenClause(self, ctx:WFLParser.ThenClauseContext):
        pass

    # Exit a parse tree produced by WFLParser#thenClause.
    def exitThenClause(self, ctx:WFLParser.ThenClauseContext):
        pass


    # Enter a parse tree produced by WFLParser#elseClause.
    def enterElseClause(self, ctx:WFLParser.ElseClauseContext):
        pass

    # Exit a parse tree produced by WFLParser#elseClause.
    def exitElseClause(self, ctx:WFLParser.ElseClauseContext):
        pass


    # Enter a parse tree produced by WFLParser#booleanExpression.
    def enterBooleanExpression(self, ctx:WFLParser.BooleanExpressionContext):
        pass

    # Exit a parse tree produced by WFLParser#booleanExpression.
    def exitBooleanExpression(self, ctx:WFLParser.BooleanExpressionContext):
        pass


    # Enter a parse tree produced by WFLParser#booleanComparison.
    def enterBooleanComparison(self, ctx:WFLParser.BooleanComparisonContext):
        pass

    # Exit a parse tree produced by WFLParser#booleanComparison.
    def exitBooleanComparison(self, ctx:WFLParser.BooleanComparisonContext):
        pass


    # Enter a parse tree produced by WFLParser#storageUnit.
    def enterStorageUnit(self, ctx:WFLParser.StorageUnitContext):
        pass

    # Exit a parse tree produced by WFLParser#storageUnit.
    def exitStorageUnit(self, ctx:WFLParser.StorageUnitContext):
        pass


    # Enter a parse tree produced by WFLParser#doStatement.
    def enterDoStatement(self, ctx:WFLParser.DoStatementContext):
        pass

    # Exit a parse tree produced by WFLParser#doStatement.
    def exitDoStatement(self, ctx:WFLParser.DoStatementContext):
        pass


    # Enter a parse tree produced by WFLParser#whileStatement.
    def enterWhileStatement(self, ctx:WFLParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by WFLParser#whileStatement.
    def exitWhileStatement(self, ctx:WFLParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by WFLParser#caseStatement.
    def enterCaseStatement(self, ctx:WFLParser.CaseStatementContext):
        pass

    # Exit a parse tree produced by WFLParser#caseStatement.
    def exitCaseStatement(self, ctx:WFLParser.CaseStatementContext):
        pass


    # Enter a parse tree produced by WFLParser#caseExpression.
    def enterCaseExpression(self, ctx:WFLParser.CaseExpressionContext):
        pass

    # Exit a parse tree produced by WFLParser#caseExpression.
    def exitCaseExpression(self, ctx:WFLParser.CaseExpressionContext):
        pass


    # Enter a parse tree produced by WFLParser#caseClauses.
    def enterCaseClauses(self, ctx:WFLParser.CaseClausesContext):
        pass

    # Exit a parse tree produced by WFLParser#caseClauses.
    def exitCaseClauses(self, ctx:WFLParser.CaseClausesContext):
        pass


    # Enter a parse tree produced by WFLParser#caseClause.
    def enterCaseClause(self, ctx:WFLParser.CaseClauseContext):
        pass

    # Exit a parse tree produced by WFLParser#caseClause.
    def exitCaseClause(self, ctx:WFLParser.CaseClauseContext):
        pass


    # Enter a parse tree produced by WFLParser#caseConstantExpression.
    def enterCaseConstantExpression(self, ctx:WFLParser.CaseConstantExpressionContext):
        pass

    # Exit a parse tree produced by WFLParser#caseConstantExpression.
    def exitCaseConstantExpression(self, ctx:WFLParser.CaseConstantExpressionContext):
        pass


    # Enter a parse tree produced by WFLParser#alterStatement.
    def enterAlterStatement(self, ctx:WFLParser.AlterStatementContext):
        pass

    # Exit a parse tree produced by WFLParser#alterStatement.
    def exitAlterStatement(self, ctx:WFLParser.AlterStatementContext):
        pass


    # Enter a parse tree produced by WFLParser#longFileTitle.
    def enterLongFileTitle(self, ctx:WFLParser.LongFileTitleContext):
        pass

    # Exit a parse tree produced by WFLParser#longFileTitle.
    def exitLongFileTitle(self, ctx:WFLParser.LongFileTitleContext):
        pass


    # Enter a parse tree produced by WFLParser#longDirectoryTitle.
    def enterLongDirectoryTitle(self, ctx:WFLParser.LongDirectoryTitleContext):
        pass

    # Exit a parse tree produced by WFLParser#longDirectoryTitle.
    def exitLongDirectoryTitle(self, ctx:WFLParser.LongDirectoryTitleContext):
        pass


    # Enter a parse tree produced by WFLParser#alterAttributeList.
    def enterAlterAttributeList(self, ctx:WFLParser.AlterAttributeListContext):
        pass

    # Exit a parse tree produced by WFLParser#alterAttributeList.
    def exitAlterAttributeList(self, ctx:WFLParser.AlterAttributeListContext):
        pass


    # Enter a parse tree produced by WFLParser#alterAttribute.
    def enterAlterAttribute(self, ctx:WFLParser.AlterAttributeContext):
        pass

    # Exit a parse tree produced by WFLParser#alterAttribute.
    def exitAlterAttribute(self, ctx:WFLParser.AlterAttributeContext):
        pass


    # Enter a parse tree produced by WFLParser#alternategroupsValue.
    def enterAlternategroupsValue(self, ctx:WFLParser.AlternategroupsValueContext):
        pass

    # Exit a parse tree produced by WFLParser#alternategroupsValue.
    def exitAlternategroupsValue(self, ctx:WFLParser.AlternategroupsValueContext):
        pass


    # Enter a parse tree produced by WFLParser#groupExpression.
    def enterGroupExpression(self, ctx:WFLParser.GroupExpressionContext):
        pass

    # Exit a parse tree produced by WFLParser#groupExpression.
    def exitGroupExpression(self, ctx:WFLParser.GroupExpressionContext):
        pass


    # Enter a parse tree produced by WFLParser#mnemonicValue.
    def enterMnemonicValue(self, ctx:WFLParser.MnemonicValueContext):
        pass

    # Exit a parse tree produced by WFLParser#mnemonicValue.
    def exitMnemonicValue(self, ctx:WFLParser.MnemonicValueContext):
        pass


    # Enter a parse tree produced by WFLParser#fileMnemonicPrimary.
    def enterFileMnemonicPrimary(self, ctx:WFLParser.FileMnemonicPrimaryContext):
        pass

    # Exit a parse tree produced by WFLParser#fileMnemonicPrimary.
    def exitFileMnemonicPrimary(self, ctx:WFLParser.FileMnemonicPrimaryContext):
        pass


    # Enter a parse tree produced by WFLParser#nameConstant.
    def enterNameConstant(self, ctx:WFLParser.NameConstantContext):
        pass

    # Exit a parse tree produced by WFLParser#nameConstant.
    def exitNameConstant(self, ctx:WFLParser.NameConstantContext):
        pass


    # Enter a parse tree produced by WFLParser#mnemonic.
    def enterMnemonic(self, ctx:WFLParser.MnemonicContext):
        pass

    # Exit a parse tree produced by WFLParser#mnemonic.
    def exitMnemonic(self, ctx:WFLParser.MnemonicContext):
        pass


    # Enter a parse tree produced by WFLParser#changeStatement.
    def enterChangeStatement(self, ctx:WFLParser.ChangeStatementContext):
        pass

    # Exit a parse tree produced by WFLParser#changeStatement.
    def exitChangeStatement(self, ctx:WFLParser.ChangeStatementContext):
        pass


    # Enter a parse tree produced by WFLParser#changeItem.
    def enterChangeItem(self, ctx:WFLParser.ChangeItemContext):
        pass

    # Exit a parse tree produced by WFLParser#changeItem.
    def exitChangeItem(self, ctx:WFLParser.ChangeItemContext):
        pass


    # Enter a parse tree produced by WFLParser#crunchStatement.
    def enterCrunchStatement(self, ctx:WFLParser.CrunchStatementContext):
        pass

    # Exit a parse tree produced by WFLParser#crunchStatement.
    def exitCrunchStatement(self, ctx:WFLParser.CrunchStatementContext):
        pass


    # Enter a parse tree produced by WFLParser#goStatement.
    def enterGoStatement(self, ctx:WFLParser.GoStatementContext):
        pass

    # Exit a parse tree produced by WFLParser#goStatement.
    def exitGoStatement(self, ctx:WFLParser.GoStatementContext):
        pass


    # Enter a parse tree produced by WFLParser#labelIdentifer.
    def enterLabelIdentifer(self, ctx:WFLParser.LabelIdentiferContext):
        pass

    # Exit a parse tree produced by WFLParser#labelIdentifer.
    def exitLabelIdentifer(self, ctx:WFLParser.LabelIdentiferContext):
        pass


    # Enter a parse tree produced by WFLParser#modifyStatement.
    def enterModifyStatement(self, ctx:WFLParser.ModifyStatementContext):
        pass

    # Exit a parse tree produced by WFLParser#modifyStatement.
    def exitModifyStatement(self, ctx:WFLParser.ModifyStatementContext):
        pass


    # Enter a parse tree produced by WFLParser#onClause.
    def enterOnClause(self, ctx:WFLParser.OnClauseContext):
        pass

    # Exit a parse tree produced by WFLParser#onClause.
    def exitOnClause(self, ctx:WFLParser.OnClauseContext):
        pass


    # Enter a parse tree produced by WFLParser#removeStatement.
    def enterRemoveStatement(self, ctx:WFLParser.RemoveStatementContext):
        pass

    # Exit a parse tree produced by WFLParser#removeStatement.
    def exitRemoveStatement(self, ctx:WFLParser.RemoveStatementContext):
        pass


    # Enter a parse tree produced by WFLParser#fromClause.
    def enterFromClause(self, ctx:WFLParser.FromClauseContext):
        pass

    # Exit a parse tree produced by WFLParser#fromClause.
    def exitFromClause(self, ctx:WFLParser.FromClauseContext):
        pass


    # Enter a parse tree produced by WFLParser#fromClauseParameter.
    def enterFromClauseParameter(self, ctx:WFLParser.FromClauseParameterContext):
        pass

    # Exit a parse tree produced by WFLParser#fromClauseParameter.
    def exitFromClauseParameter(self, ctx:WFLParser.FromClauseParameterContext):
        pass


    # Enter a parse tree produced by WFLParser#toClause.
    def enterToClause(self, ctx:WFLParser.ToClauseContext):
        pass

    # Exit a parse tree produced by WFLParser#toClause.
    def exitToClause(self, ctx:WFLParser.ToClauseContext):
        pass


    # Enter a parse tree produced by WFLParser#toClauseParameters.
    def enterToClauseParameters(self, ctx:WFLParser.ToClauseParametersContext):
        pass

    # Exit a parse tree produced by WFLParser#toClauseParameters.
    def exitToClauseParameters(self, ctx:WFLParser.ToClauseParametersContext):
        pass


    # Enter a parse tree produced by WFLParser#onStatement.
    def enterOnStatement(self, ctx:WFLParser.OnStatementContext):
        pass

    # Exit a parse tree produced by WFLParser#onStatement.
    def exitOnStatement(self, ctx:WFLParser.OnStatementContext):
        pass


    # Enter a parse tree produced by WFLParser#intoClause.
    def enterIntoClause(self, ctx:WFLParser.IntoClauseContext):
        pass

    # Exit a parse tree produced by WFLParser#intoClause.
    def exitIntoClause(self, ctx:WFLParser.IntoClauseContext):
        pass


    # Enter a parse tree produced by WFLParser#openStatement.
    def enterOpenStatement(self, ctx:WFLParser.OpenStatementContext):
        pass

    # Exit a parse tree produced by WFLParser#openStatement.
    def exitOpenStatement(self, ctx:WFLParser.OpenStatementContext):
        pass


    # Enter a parse tree produced by WFLParser#lockStatement.
    def enterLockStatement(self, ctx:WFLParser.LockStatementContext):
        pass

    # Exit a parse tree produced by WFLParser#lockStatement.
    def exitLockStatement(self, ctx:WFLParser.LockStatementContext):
        pass


    # Enter a parse tree produced by WFLParser#releaseStatement.
    def enterReleaseStatement(self, ctx:WFLParser.ReleaseStatementContext):
        pass

    # Exit a parse tree produced by WFLParser#releaseStatement.
    def exitReleaseStatement(self, ctx:WFLParser.ReleaseStatementContext):
        pass


    # Enter a parse tree produced by WFLParser#replaceStatement.
    def enterReplaceStatement(self, ctx:WFLParser.ReplaceStatementContext):
        pass

    # Exit a parse tree produced by WFLParser#replaceStatement.
    def exitReplaceStatement(self, ctx:WFLParser.ReplaceStatementContext):
        pass


    # Enter a parse tree produced by WFLParser#replaceOptions.
    def enterReplaceOptions(self, ctx:WFLParser.ReplaceOptionsContext):
        pass

    # Exit a parse tree produced by WFLParser#replaceOptions.
    def exitReplaceOptions(self, ctx:WFLParser.ReplaceOptionsContext):
        pass


    # Enter a parse tree produced by WFLParser#subroutineInvocationStatement.
    def enterSubroutineInvocationStatement(self, ctx:WFLParser.SubroutineInvocationStatementContext):
        pass

    # Exit a parse tree produced by WFLParser#subroutineInvocationStatement.
    def exitSubroutineInvocationStatement(self, ctx:WFLParser.SubroutineInvocationStatementContext):
        pass


    # Enter a parse tree produced by WFLParser#subroutineIdentifier.
    def enterSubroutineIdentifier(self, ctx:WFLParser.SubroutineIdentifierContext):
        pass

    # Exit a parse tree produced by WFLParser#subroutineIdentifier.
    def exitSubroutineIdentifier(self, ctx:WFLParser.SubroutineIdentifierContext):
        pass


    # Enter a parse tree produced by WFLParser#argumentList.
    def enterArgumentList(self, ctx:WFLParser.ArgumentListContext):
        pass

    # Exit a parse tree produced by WFLParser#argumentList.
    def exitArgumentList(self, ctx:WFLParser.ArgumentListContext):
        pass


    # Enter a parse tree produced by WFLParser#argument.
    def enterArgument(self, ctx:WFLParser.ArgumentContext):
        pass

    # Exit a parse tree produced by WFLParser#argument.
    def exitArgument(self, ctx:WFLParser.ArgumentContext):
        pass


    # Enter a parse tree produced by WFLParser#charDataKeyword.
    def enterCharDataKeyword(self, ctx:WFLParser.CharDataKeywordContext):
        pass

    # Exit a parse tree produced by WFLParser#charDataKeyword.
    def exitCharDataKeyword(self, ctx:WFLParser.CharDataKeywordContext):
        pass



del WFLParser