# Generated from grammar/wfl/WFL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .WFLParser import WFLParser
else:
    from WFLParser import WFLParser

# This class defines a complete generic visitor for a parse tree produced by WFLParser.

class WFLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by WFLParser#startRule.
    def visitStartRule(self, ctx:WFLParser.StartRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#job.
    def visitJob(self, ctx:WFLParser.JobContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#beginJob.
    def visitBeginJob(self, ctx:WFLParser.BeginJobContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#hostname.
    def visitHostname(self, ctx:WFLParser.HostnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#parameters.
    def visitParameters(self, ctx:WFLParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#parameterList.
    def visitParameterList(self, ctx:WFLParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#parameter.
    def visitParameter(self, ctx:WFLParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#parameterDefaultValue.
    def visitParameterDefaultValue(self, ctx:WFLParser.ParameterDefaultValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#dataType.
    def visitDataType(self, ctx:WFLParser.DataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#endJob.
    def visitEndJob(self, ctx:WFLParser.EndJobContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#filePath.
    def visitFilePath(self, ctx:WFLParser.FilePathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#equal.
    def visitEqual(self, ctx:WFLParser.EqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#filePathName.
    def visitFilePathName(self, ctx:WFLParser.FilePathNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#filePathNameChar.
    def visitFilePathNameChar(self, ctx:WFLParser.FilePathNameCharContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#attributes.
    def visitAttributes(self, ctx:WFLParser.AttributesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#attribute.
    def visitAttribute(self, ctx:WFLParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#stackLimitAttribute.
    def visitStackLimitAttribute(self, ctx:WFLParser.StackLimitAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#optionsAttribute.
    def visitOptionsAttribute(self, ctx:WFLParser.OptionsAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#optionList.
    def visitOptionList(self, ctx:WFLParser.OptionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#option.
    def visitOption(self, ctx:WFLParser.OptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#languageAttribute.
    def visitLanguageAttribute(self, ctx:WFLParser.LanguageAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#bdNameAttribute.
    def visitBdNameAttribute(self, ctx:WFLParser.BdNameAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#startTimeAttribute.
    def visitStartTimeAttribute(self, ctx:WFLParser.StartTimeAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#startTimeSpec.
    def visitStartTimeSpec(self, ctx:WFLParser.StartTimeSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#time.
    def visitTime(self, ctx:WFLParser.TimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#timeInterval.
    def visitTimeInterval(self, ctx:WFLParser.TimeIntervalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#date.
    def visitDate(self, ctx:WFLParser.DateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#dayOfWeek.
    def visitDayOfWeek(self, ctx:WFLParser.DayOfWeekContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#month.
    def visitMonth(self, ctx:WFLParser.MonthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#mm.
    def visitMm(self, ctx:WFLParser.MmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#dd.
    def visitDd(self, ctx:WFLParser.DdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#yy.
    def visitYy(self, ctx:WFLParser.YyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#yyyy.
    def visitYyyy(self, ctx:WFLParser.YyyyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#yyddd.
    def visitYyddd(self, ctx:WFLParser.YydddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#yyyyddd.
    def visitYyyyddd(self, ctx:WFLParser.YyyydddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#dayInterval.
    def visitDayInterval(self, ctx:WFLParser.DayIntervalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#fetchAttribute.
    def visitFetchAttribute(self, ctx:WFLParser.FetchAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#maxIOTimeAttribute.
    def visitMaxIOTimeAttribute(self, ctx:WFLParser.MaxIOTimeAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#maxLinesAttribute.
    def visitMaxLinesAttribute(self, ctx:WFLParser.MaxLinesAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#maxProcTimeAttribute.
    def visitMaxProcTimeAttribute(self, ctx:WFLParser.MaxProcTimeAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#maxWaitAttribute.
    def visitMaxWaitAttribute(self, ctx:WFLParser.MaxWaitAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#elapsedLimitAttribute.
    def visitElapsedLimitAttribute(self, ctx:WFLParser.ElapsedLimitAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#familyAttribute.
    def visitFamilyAttribute(self, ctx:WFLParser.FamilyAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#reservedKeyword.
    def visitReservedKeyword(self, ctx:WFLParser.ReservedKeywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#accessCodeAttribute.
    def visitAccessCodeAttribute(self, ctx:WFLParser.AccessCodeAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#userAttribute.
    def visitUserAttribute(self, ctx:WFLParser.UserAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#userCodeAttribute.
    def visitUserCodeAttribute(self, ctx:WFLParser.UserCodeAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#classAttribute.
    def visitClassAttribute(self, ctx:WFLParser.ClassAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#priorityAttribute.
    def visitPriorityAttribute(self, ctx:WFLParser.PriorityAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#chargeCodeAttribute.
    def visitChargeCodeAttribute(self, ctx:WFLParser.ChargeCodeAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#declarations.
    def visitDeclarations(self, ctx:WFLParser.DeclarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#declaration.
    def visitDeclaration(self, ctx:WFLParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#dataDeclaration.
    def visitDataDeclaration(self, ctx:WFLParser.DataDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#dataFilePathDelaration.
    def visitDataFilePathDelaration(self, ctx:WFLParser.DataFilePathDelarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#dataShowName.
    def visitDataShowName(self, ctx:WFLParser.DataShowNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#dataSystemClause.
    def visitDataSystemClause(self, ctx:WFLParser.DataSystemClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#dataSpecification.
    def visitDataSpecification(self, ctx:WFLParser.DataSpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#dataSpecificationAssignment.
    def visitDataSpecificationAssignment(self, ctx:WFLParser.DataSpecificationAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#dataSpecificationSection.
    def visitDataSpecificationSection(self, ctx:WFLParser.DataSpecificationSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#dataSpecificationEntry.
    def visitDataSpecificationEntry(self, ctx:WFLParser.DataSpecificationEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#dataSpecificationSectionType.
    def visitDataSpecificationSectionType(self, ctx:WFLParser.DataSpecificationSectionTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#dataSpecificationSectionName.
    def visitDataSpecificationSectionName(self, ctx:WFLParser.DataSpecificationSectionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#dataSpecificationAttribute.
    def visitDataSpecificationAttribute(self, ctx:WFLParser.DataSpecificationAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#dataSpecificationValue.
    def visitDataSpecificationValue(self, ctx:WFLParser.DataSpecificationValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#dataUseClause.
    def visitDataUseClause(self, ctx:WFLParser.DataUseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#dataUseClauseComponent.
    def visitDataUseClauseComponent(self, ctx:WFLParser.DataUseClauseComponentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#headingComponent.
    def visitHeadingComponent(self, ctx:WFLParser.HeadingComponentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#pageComponent.
    def visitPageComponent(self, ctx:WFLParser.PageComponentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#includeComponent.
    def visitIncludeComponent(self, ctx:WFLParser.IncludeComponentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#excludeComponent.
    def visitExcludeComponent(self, ctx:WFLParser.ExcludeComponentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#outputComponent.
    def visitOutputComponent(self, ctx:WFLParser.OutputComponentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#reportsComponent.
    def visitReportsComponent(self, ctx:WFLParser.ReportsComponentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#outputItems.
    def visitOutputItems(self, ctx:WFLParser.OutputItemsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#useComponent.
    def visitUseComponent(self, ctx:WFLParser.UseComponentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#reportComponent.
    def visitReportComponent(self, ctx:WFLParser.ReportComponentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#sourceComponent.
    def visitSourceComponent(self, ctx:WFLParser.SourceComponentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#sortByComponent.
    def visitSortByComponent(self, ctx:WFLParser.SortByComponentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#sortByParam.
    def visitSortByParam(self, ctx:WFLParser.SortByParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#breakComponent.
    def visitBreakComponent(self, ctx:WFLParser.BreakComponentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#breakOnParam.
    def visitBreakOnParam(self, ctx:WFLParser.BreakOnParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#totalling.
    def visitTotalling(self, ctx:WFLParser.TotallingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#totallingParam.
    def visitTotallingParam(self, ctx:WFLParser.TotallingParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#databaseClause.
    def visitDatabaseClause(self, ctx:WFLParser.DatabaseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#databaseMalnipulationOptions.
    def visitDatabaseMalnipulationOptions(self, ctx:WFLParser.DatabaseMalnipulationOptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#otherDatabaseClauseInput.
    def visitOtherDatabaseClauseInput(self, ctx:WFLParser.OtherDatabaseClauseInputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#datasetClause.
    def visitDatasetClause(self, ctx:WFLParser.DatasetClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#datasetDbDeclaration.
    def visitDatasetDbDeclaration(self, ctx:WFLParser.DatasetDbDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#datasetDatasetDeclaration.
    def visitDatasetDatasetDeclaration(self, ctx:WFLParser.DatasetDatasetDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#datasetFileDeclaration.
    def visitDatasetFileDeclaration(self, ctx:WFLParser.DatasetFileDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#datasetRecordDeclaration.
    def visitDatasetRecordDeclaration(self, ctx:WFLParser.DatasetRecordDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#datasetSourceDeclaration.
    def visitDatasetSourceDeclaration(self, ctx:WFLParser.DatasetSourceDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#datasetLoadDeclaration.
    def visitDatasetLoadDeclaration(self, ctx:WFLParser.DatasetLoadDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#dataUserAndAccessCodeListClause.
    def visitDataUserAndAccessCodeListClause(self, ctx:WFLParser.DataUserAndAccessCodeListClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#setMergeLabelsintable.
    def visitSetMergeLabelsintable(self, ctx:WFLParser.SetMergeLabelsintableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#setMergeResetList.
    def visitSetMergeResetList(self, ctx:WFLParser.SetMergeResetListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#updateClause.
    def visitUpdateClause(self, ctx:WFLParser.UpdateClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#resetZipClause.
    def visitResetZipClause(self, ctx:WFLParser.ResetZipClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#globalAndResourseSetting.
    def visitGlobalAndResourseSetting(self, ctx:WFLParser.GlobalAndResourseSettingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#nopostdumpConfig.
    def visitNopostdumpConfig(self, ctx:WFLParser.NopostdumpConfigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#globalConfig.
    def visitGlobalConfig(self, ctx:WFLParser.GlobalConfigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#internalFileConfig.
    def visitInternalFileConfig(self, ctx:WFLParser.InternalFileConfigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#allowedCoreConfig.
    def visitAllowedCoreConfig(self, ctx:WFLParser.AllowedCoreConfigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#setListZipClause.
    def visitSetListZipClause(self, ctx:WFLParser.SetListZipClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#setListClause.
    def visitSetListClause(self, ctx:WFLParser.SetListClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#generateBlock.
    def visitGenerateBlock(self, ctx:WFLParser.GenerateBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#generateParameters.
    def visitGenerateParameters(self, ctx:WFLParser.GenerateParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#generateNonCopyParameters.
    def visitGenerateNonCopyParameters(self, ctx:WFLParser.GenerateNonCopyParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#generateNonCopyParameter.
    def visitGenerateNonCopyParameter(self, ctx:WFLParser.GenerateNonCopyParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#generateCopyParameters.
    def visitGenerateCopyParameters(self, ctx:WFLParser.GenerateCopyParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#generateCopyParameter.
    def visitGenerateCopyParameter(self, ctx:WFLParser.GenerateCopyParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#orderByClause.
    def visitOrderByClause(self, ctx:WFLParser.OrderByClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#databaseDeclaration.
    def visitDatabaseDeclaration(self, ctx:WFLParser.DatabaseDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#databaseOptions.
    def visitDatabaseOptions(self, ctx:WFLParser.DatabaseOptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#databaseOption.
    def visitDatabaseOption(self, ctx:WFLParser.DatabaseOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#dumpDeclaration.
    def visitDumpDeclaration(self, ctx:WFLParser.DumpDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#dumpParameters.
    def visitDumpParameters(self, ctx:WFLParser.DumpParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#dumpParameter.
    def visitDumpParameter(self, ctx:WFLParser.DumpParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#includeDeclaration.
    def visitIncludeDeclaration(self, ctx:WFLParser.IncludeDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#taskDeclaration.
    def visitTaskDeclaration(self, ctx:WFLParser.TaskDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#taskIdentifierDeclaration.
    def visitTaskIdentifierDeclaration(self, ctx:WFLParser.TaskIdentifierDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#myselfTaskAssignment.
    def visitMyselfTaskAssignment(self, ctx:WFLParser.MyselfTaskAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#myjobTaskAssignment.
    def visitMyjobTaskAssignment(self, ctx:WFLParser.MyjobTaskAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#taskIdentifier.
    def visitTaskIdentifier(self, ctx:WFLParser.TaskIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#taskIdentifierAssigments.
    def visitTaskIdentifierAssigments(self, ctx:WFLParser.TaskIdentifierAssigmentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#taskIdentifierAssigment.
    def visitTaskIdentifierAssigment(self, ctx:WFLParser.TaskIdentifierAssigmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#fileEquation.
    def visitFileEquation(self, ctx:WFLParser.FileEquationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#fileAttributeAssignment.
    def visitFileAttributeAssignment(self, ctx:WFLParser.FileAttributeAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#fileAttribute.
    def visitFileAttribute(self, ctx:WFLParser.FileAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#booleanFileAttribute.
    def visitBooleanFileAttribute(self, ctx:WFLParser.BooleanFileAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#integerFileAttribute.
    def visitIntegerFileAttribute(self, ctx:WFLParser.IntegerFileAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#stringFileAttribute.
    def visitStringFileAttribute(self, ctx:WFLParser.StringFileAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#titleFileAttribute.
    def visitTitleFileAttribute(self, ctx:WFLParser.TitleFileAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#blockSizeFileAttribute.
    def visitBlockSizeFileAttribute(self, ctx:WFLParser.BlockSizeFileAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#fileNameFileAttribute.
    def visitFileNameFileAttribute(self, ctx:WFLParser.FileNameFileAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#longFileNameFileAttribute.
    def visitLongFileNameFileAttribute(self, ctx:WFLParser.LongFileNameFileAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#longTitleFileAttribute.
    def visitLongTitleFileAttribute(self, ctx:WFLParser.LongTitleFileAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#mnemonicFileAttribute.
    def visitMnemonicFileAttribute(self, ctx:WFLParser.MnemonicFileAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#deviceKindAssigment.
    def visitDeviceKindAssigment(self, ctx:WFLParser.DeviceKindAssigmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#serialNumberAssigment.
    def visitSerialNumberAssigment(self, ctx:WFLParser.SerialNumberAssigmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#fileAttributeValue.
    def visitFileAttributeValue(self, ctx:WFLParser.FileAttributeValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#taskAttributeAssignment.
    def visitTaskAttributeAssignment(self, ctx:WFLParser.TaskAttributeAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#taskAttribute.
    def visitTaskAttribute(self, ctx:WFLParser.TaskAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#taskAttributeValue.
    def visitTaskAttributeValue(self, ctx:WFLParser.TaskAttributeValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#fileDeclaration.
    def visitFileDeclaration(self, ctx:WFLParser.FileDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#fileDeclarationElement.
    def visitFileDeclarationElement(self, ctx:WFLParser.FileDeclarationElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#booleanDeclaration.
    def visitBooleanDeclaration(self, ctx:WFLParser.BooleanDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#booleanDeclarationElement.
    def visitBooleanDeclarationElement(self, ctx:WFLParser.BooleanDeclarationElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#booleanConstantExpression.
    def visitBooleanConstantExpression(self, ctx:WFLParser.BooleanConstantExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#integerDeclaration.
    def visitIntegerDeclaration(self, ctx:WFLParser.IntegerDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#integerDeclarationElement.
    def visitIntegerDeclarationElement(self, ctx:WFLParser.IntegerDeclarationElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#integerConstantExpression.
    def visitIntegerConstantExpression(self, ctx:WFLParser.IntegerConstantExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#realDeclaration.
    def visitRealDeclaration(self, ctx:WFLParser.RealDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#realDeclarationElement.
    def visitRealDeclarationElement(self, ctx:WFLParser.RealDeclarationElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#realConstantExpression.
    def visitRealConstantExpression(self, ctx:WFLParser.RealConstantExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#stringDeclaration.
    def visitStringDeclaration(self, ctx:WFLParser.StringDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#stringDeclarationElement.
    def visitStringDeclarationElement(self, ctx:WFLParser.StringDeclarationElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#stringConstantExpression.
    def visitStringConstantExpression(self, ctx:WFLParser.StringConstantExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#primaryStringExpression.
    def visitPrimaryStringExpression(self, ctx:WFLParser.PrimaryStringExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#stringFunction.
    def visitStringFunction(self, ctx:WFLParser.StringFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#parameterReference.
    def visitParameterReference(self, ctx:WFLParser.ParameterReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#constantDeclaration.
    def visitConstantDeclaration(self, ctx:WFLParser.ConstantDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#constantDeclarationElement.
    def visitConstantDeclarationElement(self, ctx:WFLParser.ConstantDeclarationElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#booleanConstantDeclaration.
    def visitBooleanConstantDeclaration(self, ctx:WFLParser.BooleanConstantDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#integerConstantDeclaration.
    def visitIntegerConstantDeclaration(self, ctx:WFLParser.IntegerConstantDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#realConstantDeclaration.
    def visitRealConstantDeclaration(self, ctx:WFLParser.RealConstantDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#stringConstantDeclaration.
    def visitStringConstantDeclaration(self, ctx:WFLParser.StringConstantDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#subroutineDeclaration.
    def visitSubroutineDeclaration(self, ctx:WFLParser.SubroutineDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#subroutineName.
    def visitSubroutineName(self, ctx:WFLParser.SubroutineNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#subroutineParameters.
    def visitSubroutineParameters(self, ctx:WFLParser.SubroutineParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#subroutineParameterList.
    def visitSubroutineParameterList(self, ctx:WFLParser.SubroutineParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#subroutineParameter.
    def visitSubroutineParameter(self, ctx:WFLParser.SubroutineParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#booleanParameter.
    def visitBooleanParameter(self, ctx:WFLParser.BooleanParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#integerParameter.
    def visitIntegerParameter(self, ctx:WFLParser.IntegerParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#realParameter.
    def visitRealParameter(self, ctx:WFLParser.RealParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#stringParameter.
    def visitStringParameter(self, ctx:WFLParser.StringParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#fileParameter.
    def visitFileParameter(self, ctx:WFLParser.FileParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#taskParameter.
    def visitTaskParameter(self, ctx:WFLParser.TaskParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#subroutineBlock.
    def visitSubroutineBlock(self, ctx:WFLParser.SubroutineBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#fileReferencedVariable.
    def visitFileReferencedVariable(self, ctx:WFLParser.FileReferencedVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#label.
    def visitLabel(self, ctx:WFLParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#statements.
    def visitStatements(self, ctx:WFLParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#statement.
    def visitStatement(self, ctx:WFLParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#startAndWaitStatement.
    def visitStartAndWaitStatement(self, ctx:WFLParser.StartAndWaitStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#wrapAndCompressStatement.
    def visitWrapAndCompressStatement(self, ctx:WFLParser.WrapAndCompressStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#wrapAndCompressFrom.
    def visitWrapAndCompressFrom(self, ctx:WFLParser.WrapAndCompressFromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#printStatement.
    def visitPrintStatement(self, ctx:WFLParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#printSpecification.
    def visitPrintSpecification(self, ctx:WFLParser.PrintSpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#printDefault.
    def visitPrintDefault(self, ctx:WFLParser.PrintDefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#printDefaultParameters.
    def visitPrintDefaultParameters(self, ctx:WFLParser.PrintDefaultParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#printDefaultParameter.
    def visitPrintDefaultParameter(self, ctx:WFLParser.PrintDefaultParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#printAttributeValue.
    def visitPrintAttributeValue(self, ctx:WFLParser.PrintAttributeValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#printAttribute.
    def visitPrintAttribute(self, ctx:WFLParser.PrintAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#copyAndCompareStatement.
    def visitCopyAndCompareStatement(self, ctx:WFLParser.CopyAndCompareStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#copyAndRemoveStatement.
    def visitCopyAndRemoveStatement(self, ctx:WFLParser.CopyAndRemoveStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#copyStatement.
    def visitCopyStatement(self, ctx:WFLParser.CopyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#copyProtocol.
    def visitCopyProtocol(self, ctx:WFLParser.CopyProtocolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#copyFromClause.
    def visitCopyFromClause(self, ctx:WFLParser.CopyFromClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#copyAsClause.
    def visitCopyAsClause(self, ctx:WFLParser.CopyAsClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#compileStatement.
    def visitCompileStatement(self, ctx:WFLParser.CompileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#compilerTaskEquationList.
    def visitCompilerTaskEquationList(self, ctx:WFLParser.CompilerTaskEquationListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#libraryEquation.
    def visitLibraryEquation(self, ctx:WFLParser.LibraryEquationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#databaseEquation.
    def visitDatabaseEquation(self, ctx:WFLParser.DatabaseEquationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#compilerName.
    def visitCompilerName(self, ctx:WFLParser.CompilerNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#compilerTitle.
    def visitCompilerTitle(self, ctx:WFLParser.CompilerTitleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#familyName.
    def visitFamilyName(self, ctx:WFLParser.FamilyNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#runStatement.
    def visitRunStatement(self, ctx:WFLParser.RunStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#localDataSpecification.
    def visitLocalDataSpecification(self, ctx:WFLParser.LocalDataSpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#excludeClause.
    def visitExcludeClause(self, ctx:WFLParser.ExcludeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#runParameterList.
    def visitRunParameterList(self, ctx:WFLParser.RunParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#runParameter.
    def visitRunParameter(self, ctx:WFLParser.RunParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#realExpression.
    def visitRealExpression(self, ctx:WFLParser.RealExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#integerExpression.
    def visitIntegerExpression(self, ctx:WFLParser.IntegerExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#integerMethod.
    def visitIntegerMethod(self, ctx:WFLParser.IntegerMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#otherIntegerMethod.
    def visitOtherIntegerMethod(self, ctx:WFLParser.OtherIntegerMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#integerIntegerMethod.
    def visitIntegerIntegerMethod(self, ctx:WFLParser.IntegerIntegerMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#calcExpression.
    def visitCalcExpression(self, ctx:WFLParser.CalcExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#calcExpressionTerm.
    def visitCalcExpressionTerm(self, ctx:WFLParser.CalcExpressionTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#calcExpressionFactor.
    def visitCalcExpressionFactor(self, ctx:WFLParser.CalcExpressionFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#stringExpression.
    def visitStringExpression(self, ctx:WFLParser.StringExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#stringMethod.
    def visitStringMethod(self, ctx:WFLParser.StringMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#otherStringMethod.
    def visitOtherStringMethod(self, ctx:WFLParser.OtherStringMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#acceptMethod.
    def visitAcceptMethod(self, ctx:WFLParser.AcceptMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#timeDateMethod.
    def visitTimeDateMethod(self, ctx:WFLParser.TimeDateMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#timeDateParameter.
    def visitTimeDateParameter(self, ctx:WFLParser.TimeDateParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#myselfMethod.
    def visitMyselfMethod(self, ctx:WFLParser.MyselfMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#myjobMethod.
    def visitMyjobMethod(self, ctx:WFLParser.MyjobMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#takeMethod.
    def visitTakeMethod(self, ctx:WFLParser.TakeMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#dropMethod.
    def visitDropMethod(self, ctx:WFLParser.DropMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#subStringMethod.
    def visitSubStringMethod(self, ctx:WFLParser.SubStringMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#stringStringMethod.
    def visitStringStringMethod(self, ctx:WFLParser.StringStringMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#headMethod.
    def visitHeadMethod(self, ctx:WFLParser.HeadMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#headParameter.
    def visitHeadParameter(self, ctx:WFLParser.HeadParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#tailMethod.
    def visitTailMethod(self, ctx:WFLParser.TailMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#tailParameter.
    def visitTailParameter(self, ctx:WFLParser.TailParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#concatMethod.
    def visitConcatMethod(self, ctx:WFLParser.ConcatMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#taskEquationList.
    def visitTaskEquationList(self, ctx:WFLParser.TaskEquationListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#displayStatement.
    def visitDisplayStatement(self, ctx:WFLParser.DisplayStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#initializeStatement.
    def visitInitializeStatement(self, ctx:WFLParser.InitializeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#abortStatement.
    def visitAbortStatement(self, ctx:WFLParser.AbortStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#waitStatement.
    def visitWaitStatement(self, ctx:WFLParser.WaitStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#waitContent.
    def visitWaitContent(self, ctx:WFLParser.WaitContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#waitSpecification.
    def visitWaitSpecification(self, ctx:WFLParser.WaitSpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#simpleTaskRelation.
    def visitSimpleTaskRelation(self, ctx:WFLParser.SimpleTaskRelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#taskMnemonicComparison.
    def visitTaskMnemonicComparison(self, ctx:WFLParser.TaskMnemonicComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#taskState.
    def visitTaskState(self, ctx:WFLParser.TaskStateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#booleanTaskAttribute.
    def visitBooleanTaskAttribute(self, ctx:WFLParser.BooleanTaskAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#integerTaskAttribute.
    def visitIntegerTaskAttribute(self, ctx:WFLParser.IntegerTaskAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#realTaskAttribute.
    def visitRealTaskAttribute(self, ctx:WFLParser.RealTaskAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#mnemonicTaskAttribute.
    def visitMnemonicTaskAttribute(self, ctx:WFLParser.MnemonicTaskAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#realRelation.
    def visitRealRelation(self, ctx:WFLParser.RealRelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#addStatement.
    def visitAddStatement(self, ctx:WFLParser.AddStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#addOptions.
    def visitAddOptions(self, ctx:WFLParser.AddOptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#addOption.
    def visitAddOption(self, ctx:WFLParser.AddOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#copyRequest.
    def visitCopyRequest(self, ctx:WFLParser.CopyRequestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#processStatement.
    def visitProcessStatement(self, ctx:WFLParser.ProcessStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#assignmentStatement.
    def visitAssignmentStatement(self, ctx:WFLParser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#booleanAssignmentStatement.
    def visitBooleanAssignmentStatement(self, ctx:WFLParser.BooleanAssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#booleanIdentifier.
    def visitBooleanIdentifier(self, ctx:WFLParser.BooleanIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#integerAssignmentStatement.
    def visitIntegerAssignmentStatement(self, ctx:WFLParser.IntegerAssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#integerIdentifier.
    def visitIntegerIdentifier(self, ctx:WFLParser.IntegerIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#realAssignmentStatement.
    def visitRealAssignmentStatement(self, ctx:WFLParser.RealAssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#realIdentifier.
    def visitRealIdentifier(self, ctx:WFLParser.RealIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#stringAssignmentStatement.
    def visitStringAssignmentStatement(self, ctx:WFLParser.StringAssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#stringIdentifier.
    def visitStringIdentifier(self, ctx:WFLParser.StringIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#fileAssignmentStatement.
    def visitFileAssignmentStatement(self, ctx:WFLParser.FileAssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#fileIdentifier.
    def visitFileIdentifier(self, ctx:WFLParser.FileIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#taskAssignmentStatement.
    def visitTaskAssignmentStatement(self, ctx:WFLParser.TaskAssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#startStatement.
    def visitStartStatement(self, ctx:WFLParser.StartStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#startParameterList.
    def visitStartParameterList(self, ctx:WFLParser.StartParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#namedParameterList.
    def visitNamedParameterList(self, ctx:WFLParser.NamedParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#namedParameter.
    def visitNamedParameter(self, ctx:WFLParser.NamedParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#realFormalParameter.
    def visitRealFormalParameter(self, ctx:WFLParser.RealFormalParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#integerFormalParameter.
    def visitIntegerFormalParameter(self, ctx:WFLParser.IntegerFormalParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#booleanFormalParameter.
    def visitBooleanFormalParameter(self, ctx:WFLParser.BooleanFormalParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#stringFormalParameter.
    def visitStringFormalParameter(self, ctx:WFLParser.StringFormalParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#positionalParameterList.
    def visitPositionalParameterList(self, ctx:WFLParser.PositionalParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#positionalParameter.
    def visitPositionalParameter(self, ctx:WFLParser.PositionalParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#stringPrimary.
    def visitStringPrimary(self, ctx:WFLParser.StringPrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#ifStatement.
    def visitIfStatement(self, ctx:WFLParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#condition.
    def visitCondition(self, ctx:WFLParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#simpleCondition.
    def visitSimpleCondition(self, ctx:WFLParser.SimpleConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#complexCondition.
    def visitComplexCondition(self, ctx:WFLParser.ComplexConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#combineComplexCondition.
    def visitCombineComplexCondition(self, ctx:WFLParser.CombineComplexConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#thenClause.
    def visitThenClause(self, ctx:WFLParser.ThenClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#elseClause.
    def visitElseClause(self, ctx:WFLParser.ElseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#booleanExpression.
    def visitBooleanExpression(self, ctx:WFLParser.BooleanExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#booleanComparison.
    def visitBooleanComparison(self, ctx:WFLParser.BooleanComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#storageUnit.
    def visitStorageUnit(self, ctx:WFLParser.StorageUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#doStatement.
    def visitDoStatement(self, ctx:WFLParser.DoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#whileStatement.
    def visitWhileStatement(self, ctx:WFLParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#caseStatement.
    def visitCaseStatement(self, ctx:WFLParser.CaseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#caseExpression.
    def visitCaseExpression(self, ctx:WFLParser.CaseExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#caseClauses.
    def visitCaseClauses(self, ctx:WFLParser.CaseClausesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#caseClause.
    def visitCaseClause(self, ctx:WFLParser.CaseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#caseConstantExpression.
    def visitCaseConstantExpression(self, ctx:WFLParser.CaseConstantExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#alterStatement.
    def visitAlterStatement(self, ctx:WFLParser.AlterStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#longFileTitle.
    def visitLongFileTitle(self, ctx:WFLParser.LongFileTitleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#longDirectoryTitle.
    def visitLongDirectoryTitle(self, ctx:WFLParser.LongDirectoryTitleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#alterAttributeList.
    def visitAlterAttributeList(self, ctx:WFLParser.AlterAttributeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#alterAttribute.
    def visitAlterAttribute(self, ctx:WFLParser.AlterAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#alternategroupsValue.
    def visitAlternategroupsValue(self, ctx:WFLParser.AlternategroupsValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#groupExpression.
    def visitGroupExpression(self, ctx:WFLParser.GroupExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#mnemonicValue.
    def visitMnemonicValue(self, ctx:WFLParser.MnemonicValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#fileMnemonicPrimary.
    def visitFileMnemonicPrimary(self, ctx:WFLParser.FileMnemonicPrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#nameConstant.
    def visitNameConstant(self, ctx:WFLParser.NameConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#mnemonic.
    def visitMnemonic(self, ctx:WFLParser.MnemonicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#changeStatement.
    def visitChangeStatement(self, ctx:WFLParser.ChangeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#changeItem.
    def visitChangeItem(self, ctx:WFLParser.ChangeItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#crunchStatement.
    def visitCrunchStatement(self, ctx:WFLParser.CrunchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#goStatement.
    def visitGoStatement(self, ctx:WFLParser.GoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#labelIdentifer.
    def visitLabelIdentifer(self, ctx:WFLParser.LabelIdentiferContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#modifyStatement.
    def visitModifyStatement(self, ctx:WFLParser.ModifyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#onClause.
    def visitOnClause(self, ctx:WFLParser.OnClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#removeStatement.
    def visitRemoveStatement(self, ctx:WFLParser.RemoveStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#fromClause.
    def visitFromClause(self, ctx:WFLParser.FromClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#fromClauseParameter.
    def visitFromClauseParameter(self, ctx:WFLParser.FromClauseParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#toClause.
    def visitToClause(self, ctx:WFLParser.ToClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#toClauseParameters.
    def visitToClauseParameters(self, ctx:WFLParser.ToClauseParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#onStatement.
    def visitOnStatement(self, ctx:WFLParser.OnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#intoClause.
    def visitIntoClause(self, ctx:WFLParser.IntoClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#openStatement.
    def visitOpenStatement(self, ctx:WFLParser.OpenStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#lockStatement.
    def visitLockStatement(self, ctx:WFLParser.LockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#releaseStatement.
    def visitReleaseStatement(self, ctx:WFLParser.ReleaseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#replaceStatement.
    def visitReplaceStatement(self, ctx:WFLParser.ReplaceStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#replaceOptions.
    def visitReplaceOptions(self, ctx:WFLParser.ReplaceOptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#subroutineInvocationStatement.
    def visitSubroutineInvocationStatement(self, ctx:WFLParser.SubroutineInvocationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#subroutineIdentifier.
    def visitSubroutineIdentifier(self, ctx:WFLParser.SubroutineIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#argumentList.
    def visitArgumentList(self, ctx:WFLParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#argument.
    def visitArgument(self, ctx:WFLParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WFLParser#charDataKeyword.
    def visitCharDataKeyword(self, ctx:WFLParser.CharDataKeywordContext):
        return self.visitChildren(ctx)



del WFLParser