import traceback
from typing import List
from loguru import logger

from antlr4 import ParserRuleContext
from antlr4.tree.Tree import TerminalNodeImpl

from parsers.grammar.ogl.OGLParser import OGLParser
from parsers.grammar.ogl.OGLVisitor import OGLVisitor

from parsers.grammar.ogl.ogl_schemas import (ControlCommand,
                                     OverlayCommand,
                                     OrientCommand,
                                     FontCommand,
                                     DefineGroupCommand,
                                     PositionCommand,
                                     DrawboxCommand,
                                     DrawruleCommand,
                                     PlaceCommand,
                                     SetunitsCommand,
                                     SettextCommand,
                                     DefinePatternCommand,
                                     PlacePatternCommand,SegmentCommand,
                                     BoxWithtext,
                                     Line)

from parsers.grammar.utils import (
    find_parent_by_type,
    get_original_code_content,
)

class OGLVisitorImp(OGLVisitor):


    def __init__(self):
        self.commands = []
        self.func = {
            "ControlCommandContext": self.assess_control_command,
            "OverlayCommandContext": self.assess_overlay_command,
            "OrientCommandContext": self.assess_orient_command,
            "FontCommandContext": self.assess_font_command,
            "DefineGroupCommandContext": self.assess_define_group_command,
            "PositionCommandContext": self.assess_position_command,
            "DrawboxCommandContext": self.assess_drawbox_command,
            "DrawruleCommandContext": self.assess_drawrule_command,
            "PlaceCommandContext": self.assess_place_command,
            "SetunitsCommandContext": self.assess_setunits_command,
            "SettextCommandContext": self.assess_settext_command,
            "DefinepatternCommandContext": self.assess_definepattern_command,
            "PlacePatternCommandContext": self.assess_place_pattern_command,
            "SegmentCommandContext": self.assess_segment_command,
        }

    def assess_command(self, ctx: ParserRuleContext):
        """Assess a command context and return the appropriate command object"""
        # get the type of the statement
        if isinstance(ctx, OGLParser.CommandContext):
            ctx = ctx.getChild(0)
        command_type = type(ctx).__name__
        if command_type in self.func:
            f = self.func[command_type]
            return f(ctx)
        
        logger.warning(f"Statement assessment not implemented: '{command_type}'")
        return None

    def _extract_command_metadata(self, ctx: ParserRuleContext) -> dict:
        """Extract common metadata for commands"""
        res = {}
        tag = type(ctx).__name__.replace("Context", "")
        res["tag"] = tag
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            ctx.parser, start_token.tokenIndex, stop_token.tokenIndex
        )
        return res
    
    def _append_if_top_level(self, ctx, command):
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, OGLParser.StartRuleContext):
            if command:
                self.commands.append(command)

    def assess_control_command(self, ctx:OGLParser.ControlCommandContext):
        metadata = self._extract_command_metadata(ctx)
        storage_list_ctx = ctx.controlStorage()
        message_list_ctx = ctx.controlMessage()
        summary_list_ctx = ctx.controlSummary()
        sosi_option_list_ctx = ctx.controlSosiOption()

        storages = []
        messages = []
        summaries = []
        sosi_options = []

        if storage_list_ctx:
            for storage_ctx in storage_list_ctx:
                storages.append(storage_ctx.getText())

        if message_list_ctx:
            for message_ctx in message_list_ctx:
                messages.append(message_ctx.getText())

        if summary_list_ctx:
            for summary_ctx in summary_list_ctx:
                summaries.append(summary_ctx.getText())

        if sosi_option_list_ctx:
            for sosi_ctx in sosi_option_list_ctx:
                sosi_options.append(sosi_ctx.getText())

        return ControlCommand(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="ControlCommand",
            storages=storages or None,
            messages=messages or None,
            summaries=summaries or None,
            sosi_options=sosi_options or None
        )
    def visitControlCommand(self, ctx: OGLParser.ControlCommandContext):
        try:
            control_command = self.assess_command(ctx)
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, OGLParser.StartRuleContext):
                self.commands.append(control_command)
                
        except Exception:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            logger.exception(f"Failed to assess control command: '{raw}'")
        finally:
            return self.visitChildren(ctx)


    def assess_overlay_command(self, ctx: OGLParser.OverlayCommandContext):
        metadata = self._extract_command_metadata(ctx)

        return OverlayCommand(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="OverlayCommand",
            name=ctx.overlayName().getText(),
            width=get_original_code_content(ctx.parser, ctx.overlayWidth().start.tokenIndex, ctx.overlayWidth().stop.tokenIndex),
            height=get_original_code_content(ctx.parser, ctx.overlayHeight().start.tokenIndex, ctx.overlayHeight().stop.tokenIndex),
            offset_x=get_original_code_content(ctx.parser, ctx.overlayHorizonalCoordinate().start.tokenIndex, ctx.overlayHorizonalCoordinate().stop.tokenIndex),
            offset_y=get_original_code_content(ctx.parser,ctx.overlayVerticalCoordinate().start.tokenIndex, ctx.overlayVerticalCoordinate().stop.tokenIndex),
        )
    
    def visitOverlayCommand(self, ctx: OGLParser.OverlayCommandContext):
        try:
            command = self.assess_command(ctx)
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, OGLParser.StartRuleContext):
                if command:
                    self.commands.append(command)
        except Exception:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            logger.exception(f"Failed to assess overlay command: '{raw}'")
        finally:
            return self.visitChildren(ctx)

    def assess_orient_command(self, ctx: OGLParser.OrientCommandContext):
        metadata = self._extract_command_metadata(ctx)

        return OrientCommand(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="OrientCommand",
            degree=int(ctx.orientRotatedDegree().getText())
        )
    def visitOrientCommand(self, ctx: OGLParser.OrientCommandContext):
        try:
            command = self.assess_command(ctx)
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, OGLParser.StartRuleContext):
                if command:
                    self.commands.append(command)
        except Exception:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            logger.exception(f"Failed to assess orient command: '{raw}'")
        finally:
            return self.visitChildren(ctx)


    def assess_font_command(self, ctx:OGLParser.FontCommandContext):
        metadata = self._extract_command_metadata(ctx)

        font_type = "MVS" if ctx.fontCommandMVS() else "VM"
        inner_ctx = ctx.fontCommandMVS() or ctx.fontCommandVM()

        mem_id = None
        font_name = None
        charset = None
        codepage = None
        ddname = None
        height = None
        scale = None
        color = None
        ucolor = None
        filetype = None

        if inner_ctx.fontWithMemID():
            mem_id = inner_ctx.fontWithMemID().memId().getText()
            if inner_ctx.fontWithMemID().fontName():
                font_name = inner_ctx.fontWithMemID().fontName().getText()

        if inner_ctx.fontWithCharSet():
            font_name = inner_ctx.fontWithCharSet().fontName().getText()
            charset = inner_ctx.fontWithCharSet().charSetName().getText()
            codepage = inner_ctx.fontWithCharSet().codePageName().getText()

        if hasattr(inner_ctx, "fontDDName") and inner_ctx.fontDDName():
            ddname = inner_ctx.fontDDName().ddNameName().getText()

        if hasattr(inner_ctx, "fontFileType") and inner_ctx.fontFileType():
            filetype = inner_ctx.fontFileType().fileTypeName().getText()

        if inner_ctx.fontHeight():
            height = inner_ctx.fontHeight().oglMeasurement().getText()

        if inner_ctx.fontScale():
            scale = inner_ctx.fontScale().oglMeasurement().getText()

        if inner_ctx.fontColor():
            color = inner_ctx.fontColor().fontColorName().getText()

        if inner_ctx.fontUColor():
            ucolor = inner_ctx.fontUColor().fontColorName().getText()

        return FontCommand(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="FontCommand",
            type=font_type,
            mem_id=mem_id,
            font_name=font_name,
            charset=charset,
            codepage=codepage,
            ddname=ddname,
            height=height,
            scale=scale,
            color=color,
            ucolor=ucolor,
            filetype=filetype,
        )
    def visitFontCommand(self, ctx: OGLParser.FontCommandContext):
        try:
            command = self.assess_command(ctx)
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, OGLParser.StartRuleContext):
                if command:
                    self.commands.append(command)
        except Exception:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            logger.exception(f"Failed to assess font command: '{raw}'")
        finally:
            return self.visitChildren(ctx)

        
    def assess_define_group_command(self, ctx):
        metadata = self._extract_command_metadata(ctx)

        group_name = ctx.groupName().getText()
        inner_commands = []

        for command_ctx in ctx.command():
            cmd = self.assess_command(command_ctx)
            if cmd:
                inner_commands.append(cmd)

        return DefineGroupCommand(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="DefineGroupCommand",
            group_name=group_name,
            commands=inner_commands,
        )

    def visitDefineGroupCommand(self, ctx: OGLParser.DefineGroupCommandContext):
        try:
            command = self.assess_command(ctx)
            self._append_if_top_level(ctx, command)
        except Exception:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            logger.exception(f"Failed to assess define group command: '{raw}'")
        finally:
            return self.visitChildren(ctx)

    def assess_position_command(self, ctx: OGLParser.PositionCommandContext):
        metadata = self._extract_command_metadata(ctx)

        return PositionCommand(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="PositionCommand",
            x=get_original_code_content(ctx.parser, ctx.positionX().start.tokenIndex, ctx.positionX().stop.tokenIndex),
            y=get_original_code_content(ctx.parser, ctx.positionY().start.tokenIndex, ctx.positionY().stop.tokenIndex)
        )
    
    def visitPositionCommand(self, ctx: OGLParser.PositionCommandContext):
        try:
            command = self.assess_command(ctx)
            self._append_if_top_level(ctx, command)
        except Exception:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            logger.exception(f"Failed to assess position command: '{raw}'")
        finally:
            return self.visitChildren(ctx)


    

    def assess_drawbox_command(self, ctx: OGLParser.DrawboxCommandContext):
        metadata = self._extract_command_metadata(ctx)

        width = get_original_code_content(ctx.parser, ctx.boxWidth().start.tokenIndex, ctx.boxWidth().stop.tokenIndex)
        height = get_original_code_content(ctx.parser, ctx.boxHeight().start.tokenIndex, ctx.boxHeight().stop.tokenIndex)

        border_thickness = ctx.boxBorderThickness(0).getText() if ctx.boxBorderThickness() else None
        border_type = ctx.boxBorderType(0).getText() if ctx.boxBorderType() else None

        rounded_option = None
        if ctx.boxRounded():
            rounded_ctx = ctx.boxRounded(0)
            if rounded_ctx.boxRoundedOption():
                rounded_option = get_original_code_content(
                    ctx.parser,
                    rounded_ctx.boxRoundedOption().start.tokenIndex,
                    rounded_ctx.boxRoundedOption().stop.tokenIndex
                )

        diagonal_option = None
        if ctx.boxDiagonal():
            diagonal_option = ctx.boxDiagonal(0).boxDiagonalOption().getText()

        repeat = None
        if ctx.boxRepeat():
            repeat = ctx.boxRepeat(0).getText()

        shade = None
        if ctx.boxShade():
            shade = ctx.boxShade(0).getText()

        color = None
        if ctx.boxColor():
            color = ctx.boxColor(0).getText()

        withtext = []
        ctx_withtext_list = ctx.boxWithtext()
        for withtext_ctx in ctx_withtext_list:
            box = get_original_code_content(ctx.parser, withtext_ctx.box().start.tokenIndex, withtext_ctx.box().stop.tokenIndex) if withtext_ctx.box() else None
            orient = None
            format = None
            line_spacing = None
            line = []
            if withtext_ctx.boxWithtextOrient():
                orient = withtext_ctx.boxWithtextOrient().getText()
                
            if withtext_ctx.boxWithtextFormat():
                format = withtext_ctx.boxWithtextFormat().getText()
            if withtext_ctx.boxWithtextLineSpacing():
                line_spacing = withtext_ctx.boxWithtextLineSpacing().getText()

            line_part_list_ctx = withtext_ctx.line().line_part()
            for item in line_part_list_ctx:
                line.append(Line(
                    font_name = [font_name.getText() for font_name in item.fontName()],
                    sosi_mode=item.lineSosiMode().getText() if item.lineSosiMode() else None,
                    underlying=item.lineUnderlying().getText() if item.lineUnderlying() else None,
                    text_type=item.lineTextType().getText() if item.lineTextType() else None,
                    texts=[text.getText() for text in item.text()]

                ))
            withtext.append(BoxWithtext(
                box=box,
                orient=orient,
                format=format,
                line_spacing=line_spacing,
                line=line
            ))
        return DrawboxCommand(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="DrawboxCommand",
            width=width,
            height=height,
            border_thickness=border_thickness,
            border_type=border_type,
            rounded_option=rounded_option,
            diagonal_option=diagonal_option,
            repeat=repeat,
            shade=shade,
            color=color,
            withtext=withtext,
        )


    def visitDrawboxCommand(self, ctx: OGLParser.DrawboxCommandContext):
        try:
            command = self.assess_command(ctx)
            self._append_if_top_level(ctx, command)
        except Exception:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            logger.exception(f"Failed to assess drawbox command: '{raw}'")
        finally:
            return self.visitChildren(ctx)
        
    def assess_drawrule_command(self, ctx: OGLParser.DrawruleCommandContext):
        metadata = self._extract_command_metadata(ctx)

        direction = ctx.ruleDirection().getText() if ctx.ruleDirection() else None
        length = get_original_code_content(ctx.parser, ctx.ruleLength().start.tokenIndex, ctx.ruleLength().stop.tokenIndex)
        thickness = ctx.ruleThickness().getText() if ctx.ruleThickness() else None
        rule_type = ctx.ruleType().getText() if ctx.ruleType() else None

        repeated = None
        if ctx.ruleRepeated():
            repeated = get_original_code_content(ctx.parser, ctx.ruleRepeated().start.tokenIndex, ctx.ruleRepeated().stop.tokenIndex)

        return DrawruleCommand(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="DrawruleCommand",
            direction=direction,
            length=length,
            thickness=thickness,
            rule_type=rule_type,
            repeated=repeated
        )
    def visitDrawruleCommand(self, ctx: OGLParser.DrawruleCommandContext):
        try:
            command = self.assess_command(ctx)
            self._append_if_top_level(ctx, command)
        except Exception:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            logger.exception(f"Failed to assess drawrule command: '{raw}'")
        finally:
            return self.visitChildren(ctx)




    def assess_place_command(self, ctx: OGLParser.PlaceCommandContext):
        metadata = self._extract_command_metadata(ctx)

        place_type = ctx.getChild(1).getText()
        name = ctx.groupName().getText()

        return PlaceCommand(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="PlaceCommand",
            type=place_type,
            name=name,
        )

    def visitPlaceCommand(self, ctx: OGLParser.PlaceCommandContext):
        try:
            command = self.assess_command(ctx)
            self._append_if_top_level(ctx, command)
        except Exception:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            logger.exception(f"Failed to assess place command: '{raw}'")
        finally:
            return self.visitChildren(ctx)



    def assess_setunits_command(self, ctx: OGLParser.SetunitsCommandContext):
        metadata = self._extract_command_metadata(ctx)

        default = []
        if ctx.setunitsDefault():
            default.append(ctx.setunitsDefault().primaryDefault().getText())
            if ctx.setunitsDefault().secondaryDefault():
                default.append(ctx.setunitsDefault().secondaryDefault().getText())

        linesp = ctx.setunitsLineSp().oglMeasurement().getText() if ctx.setunitsLineSp() else None
        corner_length = ctx.setunitsCornerLength().conrnerLengthValue().getText() if ctx.setunitsCornerLength() else None
        text_margin = ctx.setunitsTextMargin().textMarginValue().getText() if ctx.setunitsTextMargin() else None
        positioning = ctx.setUnitsPositioning().positionValue().getText() if ctx.setUnitsPositioning() else None

        return SetunitsCommand(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="SetunitsCommand",
            default=default if default else None,
            linesp=linesp,
            corner_length=corner_length,
            text_margin=text_margin,
            positioning=positioning
        )

    def visitSetunitsCommand(self, ctx: OGLParser.SetunitsCommandContext):
        try:
            command = self.assess_command(ctx)
            self._append_if_top_level(ctx, command)
        except Exception:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            logger.exception(f"Failed to assess setunits command: '{raw}'")
        finally:
            return self.visitChildren(ctx)


    def assess_settext_command(self, ctx: OGLParser.SettextCommandContext):
        metadata = self._extract_command_metadata(ctx)

        orientation = int(ctx.orientRotatedDegree().getText()) if ctx.orientRotatedDegree() else None
        format = ctx.settextFormat().getText() if ctx.settextFormat() else None
        alignment = None
        if ctx.settextAlignment():
            alignment = ctx.settextAlignment().getText()

        lines = [line.getText() for line in ctx.line()]

        return SettextCommand(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="SettextCommand",
            orientation=orientation,
            format=format,
            alignment=alignment,
            lines=lines,
        )

    def visitSettextCommand(self, ctx: OGLParser.SettextCommandContext):
        try:
            command = self.assess_command(ctx)
            self._append_if_top_level(ctx, command)
        except Exception:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            logger.exception(f"Failed to assess settext command: '{raw}'")
        finally:
            return self.visitChildren(ctx)


    def assess_definepattern_command(self, ctx: OGLParser.DefinepatternCommandContext):
        metadata = self._extract_command_metadata(ctx)

        return DefinePatternCommand(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="DefinePatternCommand",
            name=ctx.patternName().getText(),
            code_lines=[get_original_code_content(ctx.parser, item.start.tokenIndex, item.stop.tokenIndex) for item in ctx.lineCoding().getChild(0).coded_line()],
            code_type="PELS" if type(ctx.lineCoding().getChild(1)).__name__ == "lineCodingPels" else "ENCODED"
        )
    def visitDefinepatternCommand(self, ctx: OGLParser.DefinepatternCommandContext):
        try:
            command = self.assess_command(ctx)
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, OGLParser.StartRuleContext):
                self.commands.append(command)
        except Exception:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            logger.exception(f"Failed to assess definepattern command: '{raw}'")
        finally:
            return self.visitChildren(ctx)



    def assess_place_pattern_command(self, ctx: OGLParser.PlacePatternCommandContext):
        metadata = self._extract_command_metadata(ctx)

        return PlacePatternCommand(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="PlacePatternCommand",
            pattern_name=ctx.patternName().getText(),
            orientation=int(ctx.orientRotatedDegree().getText()) if ctx.orientRotatedDegree() else None,
            shade=[s.getText() for s in ctx.patternShade()] if ctx.patternShade() else None,
            mirror=ctx.mirrorOption().getText() if ctx.mirrorOption() else None,
            negative=ctx.negativeOption().getText() if ctx.negativeOption() else None,
            color=ctx.patternColor().patternColorName().getText() if ctx.patternColor() else None
        )

    def visitPlacePatternCommand(self, ctx: OGLParser.PlacePatternCommandContext):
        try:
            command = self.assess_command(ctx)
            self._append_if_top_level(ctx, command)
        except Exception:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            logger.exception(f"Failed to assess place pattern command: '{raw}'")
        finally:
            return self.visitChildren(ctx)


    def assess_segment_command(self, ctx: OGLParser.SegmentCommandContext):
        metadata = self._extract_command_metadata(ctx)

        name = ctx.segmentName().getText() if ctx.segmentName() else None
        mem_id = ctx.memId().getText()
        ddname = ctx.segmentDDName().segmentDDNameName().getText() if ctx.segmentDDName() else None
        filetype = ctx.segmentFileType().fileTypeName().getText() if ctx.segmentFileType() else None

        return SegmentCommand(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="SegmentCommand",
            name=name,
            mem_id=mem_id,
            ddname=ddname,
            filetype=filetype
        )

    def visitSegmentCommand(self, ctx: OGLParser.SegmentCommandContext):
        try:
            command = self.assess_command(ctx)
            self._append_if_top_level(ctx, command)
        except Exception:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            logger.exception(f"Failed to assess segment command: '{raw}'")
        finally:
            return self.visitChildren(ctx)
