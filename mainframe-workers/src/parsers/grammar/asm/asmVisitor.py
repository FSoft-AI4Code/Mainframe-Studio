# Generated from asm.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .asmParser import asmParser
else:
    from asmParser import asmParser

# This class defines a complete generic visitor for a parse tree produced by asmParser.

class asmVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by asmParser#startRule.
    def visitStartRule(self, ctx:asmParser.StartRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#line.
    def visitLine(self, ctx:asmParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#label.
    def visitLabel(self, ctx:asmParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#instruction.
    def visitInstruction(self, ctx:asmParser.InstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#load_store_instruction.
    def visitLoad_store_instruction(self, ctx:asmParser.Load_store_instructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#arithmetric_instruction.
    def visitArithmetric_instruction(self, ctx:asmParser.Arithmetric_instructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#logical_instruction.
    def visitLogical_instruction(self, ctx:asmParser.Logical_instructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#branch_instruction.
    def visitBranch_instruction(self, ctx:asmParser.Branch_instructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#decimal_instruction.
    def visitDecimal_instruction(self, ctx:asmParser.Decimal_instructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#special_instruction.
    def visitSpecial_instruction(self, ctx:asmParser.Special_instructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#assembler_instruction.
    def visitAssembler_instruction(self, ctx:asmParser.Assembler_instructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#other_instruction.
    def visitOther_instruction(self, ctx:asmParser.Other_instructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#getmain_statement.
    def visitGetmain_statement(self, ctx:asmParser.Getmain_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#getmain_params.
    def visitGetmain_params(self, ctx:asmParser.Getmain_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#getmain_param_list.
    def visitGetmain_param_list(self, ctx:asmParser.Getmain_param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#getmain_param.
    def visitGetmain_param(self, ctx:asmParser.Getmain_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#macro.
    def visitMacro(self, ctx:asmParser.MacroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#comment.
    def visitComment(self, ctx:asmParser.CommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#single_line_comment.
    def visitSingle_line_comment(self, ctx:asmParser.Single_line_commentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#multiline_comment.
    def visitMultiline_comment(self, ctx:asmParser.Multiline_commentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#operand.
    def visitOperand(self, ctx:asmParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#hash_label.
    def visitHash_label(self, ctx:asmParser.Hash_labelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#calc_expression.
    def visitCalc_expression(self, ctx:asmParser.Calc_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#addr_expression.
    def visitAddr_expression(self, ctx:asmParser.Addr_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#expression.
    def visitExpression(self, ctx:asmParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#term.
    def visitTerm(self, ctx:asmParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#displacement_expression.
    def visitDisplacement_expression(self, ctx:asmParser.Displacement_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#displacement_with_length.
    def visitDisplacement_with_length(self, ctx:asmParser.Displacement_with_lengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#character_literal.
    def visitCharacter_literal(self, ctx:asmParser.Character_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#hex_literal.
    def visitHex_literal(self, ctx:asmParser.Hex_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#halfword_literal.
    def visitHalfword_literal(self, ctx:asmParser.Halfword_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#cl_literal.
    def visitCl_literal(self, ctx:asmParser.Cl_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#xl_literal.
    def visitXl_literal(self, ctx:asmParser.Xl_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#b_literal.
    def visitB_literal(self, ctx:asmParser.B_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#f_literal.
    def visitF_literal(self, ctx:asmParser.F_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#pl_literal.
    def visitPl_literal(self, ctx:asmParser.Pl_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#memory_reference.
    def visitMemory_reference(self, ctx:asmParser.Memory_referenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#base_register_reference.
    def visitBase_register_reference(self, ctx:asmParser.Base_register_referenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#indexed_memory_reference.
    def visitIndexed_memory_reference(self, ctx:asmParser.Indexed_memory_referenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#identifier.
    def visitIdentifier(self, ctx:asmParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#symbol.
    def visitSymbol(self, ctx:asmParser.SymbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#operand_list.
    def visitOperand_list(self, ctx:asmParser.Operand_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#relative_branch.
    def visitRelative_branch(self, ctx:asmParser.Relative_branchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#register.
    def visitRegister(self, ctx:asmParser.RegisterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#ic_statement.
    def visitIc_statement(self, ctx:asmParser.Ic_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#ic_operand_list.
    def visitIc_operand_list(self, ctx:asmParser.Ic_operand_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#ic_operand.
    def visitIc_operand(self, ctx:asmParser.Ic_operandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#icm_statement.
    def visitIcm_statement(self, ctx:asmParser.Icm_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#l_statement.
    def visitL_statement(self, ctx:asmParser.L_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#number.
    def visitNumber(self, ctx:asmParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#la_statement.
    def visitLa_statement(self, ctx:asmParser.La_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#lcr_statement.
    def visitLcr_statement(self, ctx:asmParser.Lcr_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#lh_statement.
    def visitLh_statement(self, ctx:asmParser.Lh_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#lhi_statement.
    def visitLhi_statement(self, ctx:asmParser.Lhi_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#lm_statement.
    def visitLm_statement(self, ctx:asmParser.Lm_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#lnr_statement.
    def visitLnr_statement(self, ctx:asmParser.Lnr_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#lpr_statement.
    def visitLpr_statement(self, ctx:asmParser.Lpr_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#lr_statement.
    def visitLr_statement(self, ctx:asmParser.Lr_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#ltr_statement.
    def visitLtr_statement(self, ctx:asmParser.Ltr_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#mvc_statement.
    def visitMvc_statement(self, ctx:asmParser.Mvc_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#mvcl_statement.
    def visitMvcl_statement(self, ctx:asmParser.Mvcl_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#mvi_statement.
    def visitMvi_statement(self, ctx:asmParser.Mvi_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#st_statement.
    def visitSt_statement(self, ctx:asmParser.St_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#stc_statement.
    def visitStc_statement(self, ctx:asmParser.Stc_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#stcm_statement.
    def visitStcm_statement(self, ctx:asmParser.Stcm_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#sth_statement.
    def visitSth_statement(self, ctx:asmParser.Sth_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#stm_statement.
    def visitStm_statement(self, ctx:asmParser.Stm_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#a_statement.
    def visitA_statement(self, ctx:asmParser.A_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#ah_statement.
    def visitAh_statement(self, ctx:asmParser.Ah_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#ahi_statement.
    def visitAhi_statement(self, ctx:asmParser.Ahi_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#al_statement.
    def visitAl_statement(self, ctx:asmParser.Al_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#alr_statement.
    def visitAlr_statement(self, ctx:asmParser.Alr_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#ar_statement.
    def visitAr_statement(self, ctx:asmParser.Ar_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#c_statement.
    def visitC_statement(self, ctx:asmParser.C_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#ch_statement.
    def visitCh_statement(self, ctx:asmParser.Ch_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#cr_statement.
    def visitCr_statement(self, ctx:asmParser.Cr_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#cl_statement.
    def visitCl_statement(self, ctx:asmParser.Cl_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#clc_statement.
    def visitClc_statement(self, ctx:asmParser.Clc_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#clcl_statement.
    def visitClcl_statement(self, ctx:asmParser.Clcl_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#cli_statement.
    def visitCli_statement(self, ctx:asmParser.Cli_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#clm_statement.
    def visitClm_statement(self, ctx:asmParser.Clm_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#clr_statement.
    def visitClr_statement(self, ctx:asmParser.Clr_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#n_statement.
    def visitN_statement(self, ctx:asmParser.N_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#nc_statement.
    def visitNc_statement(self, ctx:asmParser.Nc_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#ni_statement.
    def visitNi_statement(self, ctx:asmParser.Ni_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#nr_statement.
    def visitNr_statement(self, ctx:asmParser.Nr_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#o_statement.
    def visitO_statement(self, ctx:asmParser.O_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#oc_statement.
    def visitOc_statement(self, ctx:asmParser.Oc_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#oi_statement.
    def visitOi_statement(self, ctx:asmParser.Oi_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#or_statement.
    def visitOr_statement(self, ctx:asmParser.Or_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#sla_statement.
    def visitSla_statement(self, ctx:asmParser.Sla_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#slda_statement.
    def visitSlda_statement(self, ctx:asmParser.Slda_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#sldl_statement.
    def visitSldl_statement(self, ctx:asmParser.Sldl_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#sll_statement.
    def visitSll_statement(self, ctx:asmParser.Sll_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#sra_statement.
    def visitSra_statement(self, ctx:asmParser.Sra_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#srda_statement.
    def visitSrda_statement(self, ctx:asmParser.Srda_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#srl_statement.
    def visitSrl_statement(self, ctx:asmParser.Srl_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#tm_statement.
    def visitTm_statement(self, ctx:asmParser.Tm_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#x_statement.
    def visitX_statement(self, ctx:asmParser.X_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#xc_statement.
    def visitXc_statement(self, ctx:asmParser.Xc_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#xi_statement.
    def visitXi_statement(self, ctx:asmParser.Xi_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#xr_statement.
    def visitXr_statement(self, ctx:asmParser.Xr_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#bal_statement.
    def visitBal_statement(self, ctx:asmParser.Bal_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#bal_operand_list.
    def visitBal_operand_list(self, ctx:asmParser.Bal_operand_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#bal_operand.
    def visitBal_operand(self, ctx:asmParser.Bal_operandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#balr_statement.
    def visitBalr_statement(self, ctx:asmParser.Balr_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#bas_statement.
    def visitBas_statement(self, ctx:asmParser.Bas_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#basr_statement.
    def visitBasr_statement(self, ctx:asmParser.Basr_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#bc_statement.
    def visitBc_statement(self, ctx:asmParser.Bc_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#bcr_statement.
    def visitBcr_statement(self, ctx:asmParser.Bcr_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#bct_statement.
    def visitBct_statement(self, ctx:asmParser.Bct_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#bctr_statement.
    def visitBctr_statement(self, ctx:asmParser.Bctr_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#bxh_statement.
    def visitBxh_statement(self, ctx:asmParser.Bxh_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#bxle_statement.
    def visitBxle_statement(self, ctx:asmParser.Bxle_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#ap_statement.
    def visitAp_statement(self, ctx:asmParser.Ap_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#cp_statement.
    def visitCp_statement(self, ctx:asmParser.Cp_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#cvp_statement.
    def visitCvp_statement(self, ctx:asmParser.Cvp_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#cvd_statement.
    def visitCvd_statement(self, ctx:asmParser.Cvd_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#dp_statement.
    def visitDp_statement(self, ctx:asmParser.Dp_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#ed_statement.
    def visitEd_statement(self, ctx:asmParser.Ed_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#edmk_statement.
    def visitEdmk_statement(self, ctx:asmParser.Edmk_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#mp_statement.
    def visitMp_statement(self, ctx:asmParser.Mp_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#mvn_statement.
    def visitMvn_statement(self, ctx:asmParser.Mvn_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#mvo_statement.
    def visitMvo_statement(self, ctx:asmParser.Mvo_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#mvz_statement.
    def visitMvz_statement(self, ctx:asmParser.Mvz_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#pack_statement.
    def visitPack_statement(self, ctx:asmParser.Pack_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#sp_statement.
    def visitSp_statement(self, ctx:asmParser.Sp_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#srp_statement.
    def visitSrp_statement(self, ctx:asmParser.Srp_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#unpk_statement.
    def visitUnpk_statement(self, ctx:asmParser.Unpk_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#zap_statement.
    def visitZap_statement(self, ctx:asmParser.Zap_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#cs_statement.
    def visitCs_statement(self, ctx:asmParser.Cs_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#cds_statement.
    def visitCds_statement(self, ctx:asmParser.Cds_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#ex_statement.
    def visitEx_statement(self, ctx:asmParser.Ex_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#stck_statement.
    def visitStck_statement(self, ctx:asmParser.Stck_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#svc_statement.
    def visitSvc_statement(self, ctx:asmParser.Svc_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#tr_statement.
    def visitTr_statement(self, ctx:asmParser.Tr_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#trt_statement.
    def visitTrt_statement(self, ctx:asmParser.Trt_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#ts_statement.
    def visitTs_statement(self, ctx:asmParser.Ts_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#amode_statement.
    def visitAmode_statement(self, ctx:asmParser.Amode_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#csect_statement.
    def visitCsect_statement(self, ctx:asmParser.Csect_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#dc_statement.
    def visitDc_statement(self, ctx:asmParser.Dc_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#dc_operand_list.
    def visitDc_operand_list(self, ctx:asmParser.Dc_operand_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#dc_operand.
    def visitDc_operand(self, ctx:asmParser.Dc_operandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#dc_constant.
    def visitDc_constant(self, ctx:asmParser.Dc_constantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#address_constant.
    def visitAddress_constant(self, ctx:asmParser.Address_constantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#dsect_statement.
    def visitDsect_statement(self, ctx:asmParser.Dsect_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#drop_statement.
    def visitDrop_statement(self, ctx:asmParser.Drop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#ejec_statement.
    def visitEjec_statement(self, ctx:asmParser.Ejec_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#end_statement.
    def visitEnd_statement(self, ctx:asmParser.End_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#equ_statement.
    def visitEqu_statement(self, ctx:asmParser.Equ_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#equ_value.
    def visitEqu_value(self, ctx:asmParser.Equ_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#ltorg_statement.
    def visitLtorg_statement(self, ctx:asmParser.Ltorg_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#org_statement.
    def visitOrg_statement(self, ctx:asmParser.Org_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#pop_statement.
    def visitPop_statement(self, ctx:asmParser.Pop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#print_statement.
    def visitPrint_statement(self, ctx:asmParser.Print_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#push_statement.
    def visitPush_statement(self, ctx:asmParser.Push_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#rmode_statement.
    def visitRmode_statement(self, ctx:asmParser.Rmode_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#space_statement.
    def visitSpace_statement(self, ctx:asmParser.Space_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#title_statement.
    def visitTitle_statement(self, ctx:asmParser.Title_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#using_statement.
    def visitUsing_statement(self, ctx:asmParser.Using_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#using_operand.
    def visitUsing_operand(self, ctx:asmParser.Using_operandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#abend_statement.
    def visitAbend_statement(self, ctx:asmParser.Abend_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#call_statement.
    def visitCall_statement(self, ctx:asmParser.Call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#call_operand_list.
    def visitCall_operand_list(self, ctx:asmParser.Call_operand_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#call_operand.
    def visitCall_operand(self, ctx:asmParser.Call_operandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#vl_operand.
    def visitVl_operand(self, ctx:asmParser.Vl_operandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#close_statement.
    def visitClose_statement(self, ctx:asmParser.Close_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#dcb_statement.
    def visitDcb_statement(self, ctx:asmParser.Dcb_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#dcb_params.
    def visitDcb_params(self, ctx:asmParser.Dcb_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#dcb_param.
    def visitDcb_param(self, ctx:asmParser.Dcb_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#dcb_key_value.
    def visitDcb_key_value(self, ctx:asmParser.Dcb_key_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#get_statement.
    def visitGet_statement(self, ctx:asmParser.Get_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#open_statement.
    def visitOpen_statement(self, ctx:asmParser.Open_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#open_operand_list.
    def visitOpen_operand_list(self, ctx:asmParser.Open_operand_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#open_operand.
    def visitOpen_operand(self, ctx:asmParser.Open_operandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#put_statement.
    def visitPut_statement(self, ctx:asmParser.Put_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#return_statement.
    def visitReturn_statement(self, ctx:asmParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#save_statement.
    def visitSave_statement(self, ctx:asmParser.Save_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#params.
    def visitParams(self, ctx:asmParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#param.
    def visitParam(self, ctx:asmParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#storage_statement.
    def visitStorage_statement(self, ctx:asmParser.Storage_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#yregs_statement.
    def visitYregs_statement(self, ctx:asmParser.Yregs_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#wto_statement.
    def visitWto_statement(self, ctx:asmParser.Wto_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#extract_statement.
    def visitExtract_statement(self, ctx:asmParser.Extract_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#display_statement.
    def visitDisplay_statement(self, ctx:asmParser.Display_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#r_register.
    def visitR_register(self, ctx:asmParser.R_registerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#display_msg.
    def visitDisplay_msg(self, ctx:asmParser.Display_msgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#cnop_statement.
    def visitCnop_statement(self, ctx:asmParser.Cnop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#comp_statement.
    def visitComp_statement(self, ctx:asmParser.Comp_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#be_statement.
    def visitBe_statement(self, ctx:asmParser.Be_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#move_statement.
    def visitMove_statement(self, ctx:asmParser.Move_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#write_statement.
    def visitWrite_statement(self, ctx:asmParser.Write_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#bh_statement.
    def visitBh_statement(self, ctx:asmParser.Bh_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#bo_statement.
    def visitBo_statement(self, ctx:asmParser.Bo_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#bl_statement.
    def visitBl_statement(self, ctx:asmParser.Bl_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#b_statement.
    def visitB_statement(self, ctx:asmParser.B_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#bne_statement.
    def visitBne_statement(self, ctx:asmParser.Bne_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#br_statement.
    def visitBr_statement(self, ctx:asmParser.Br_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#bz_statement.
    def visitBz_statement(self, ctx:asmParser.Bz_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#bnl_statement.
    def visitBnl_statement(self, ctx:asmParser.Bnl_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#slr_statement.
    def visitSlr_statement(self, ctx:asmParser.Slr_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#sr_statement.
    def visitSr_statement(self, ctx:asmParser.Sr_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#mh_statement.
    def visitMh_statement(self, ctx:asmParser.Mh_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#ds_statement.
    def visitDs_statement(self, ctx:asmParser.Ds_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#and_statement.
    def visitAnd_statement(self, ctx:asmParser.And_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asmParser#start_statement.
    def visitStart_statement(self, ctx:asmParser.Start_statementContext):
        return self.visitChildren(ctx)



del asmParser