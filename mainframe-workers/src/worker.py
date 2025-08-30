from multiprocessing import Process

import click
import structlog

from message_queue.consumers.assessment_consumer import AssessmentConsumer
from message_queue.consumers.bat_parser_consumer import BatchParserConsumer
from message_queue.consumers.bms_java_migration_consumer import \
    BMSJavaMigrationConsumer
from message_queue.consumers.bms_modernization_consumer import \
    BMSModernizationConsumer
from message_queue.consumers.bms_summarization_consumer import \
    BMSSummarizationConsumer
from message_queue.consumers.clist_dispatcher_consumer import \
    ClistDispatcherConsumer
from message_queue.consumers.clist_parser_comsumer import ClistParserConsumer
from message_queue.consumers.cobol_dispatcher_consumer import \
    CobolDispatcherConsumer
from message_queue.consumers.cobol_dnp_parser_consumer import \
    CobolDNPParserConsumer
from message_queue.consumers.cobol_java_migration_consumer import \
    CobolJavaMigrationConsumer
from message_queue.consumers.cobol_screen_summarization_consumer import \
    CobolScreenSummarizationConsumer
from message_queue.consumers.cobol_summarization_consumer import \
    CobolSummarizationConsumer
from message_queue.consumers.cobol_unisys_parser_consumer import \
    CobolUnisysParserConsumer
from message_queue.consumers.copybook_dnp_parser_consumer import \
    CopybookDNPParserConsumer
from message_queue.consumers.copybook_summarization_consumer import \
    CopybookSummarizationConsumer
from message_queue.consumers.copybook_unisys_parser_consumer import \
    CopybookUnisysParserConsumer
from message_queue.consumers.email_consumer import EmailConsumer
from message_queue.consumers.graph_consumer import GraphConsumer
from message_queue.consumers.panel_dispatcher_consumer import \
    PanelDispatcherConsumer
from message_queue.consumers.panel_parser_consumer import PanelParserConsumer
from message_queue.consumers.report_dispatcher_consumer import \
    ReportDispatcherConsumer
from message_queue.consumers.report_parser_consumer import ReportParserConsumer
from message_queue.consumers.statement_summarization_consumer import \
    StatementSummarizationConsumer
from message_queue.consumers.wfl_dispatcher_consumer import \
    WFLDispatcherConsumer
from message_queue.consumers.wfl_parser_consumer import WFLParserConsumer

logger = structlog.get_logger()

def run_clist_parser_consumer():
    """Start the Clist Parser Consumer"""
    try:
        logger.info("Starting Clist Parser Consumer")
        consumer = ClistParserConsumer()
        consumer.start_consuming()
    except Exception as e:
        logger.error("Error running Clist parser consumer", error=str(e))


def run_clist_dispatcher_consumer():
    """Start the CLIST Dispatcher Consumer"""
    try:
        logger.info("Starting CLIST Dispatcher Consumer")
        consumer = ClistDispatcherConsumer()
        consumer.start_consuming()
    except Exception as e:
        logger.error("Error running CLIST dispatcher consumer", error=str(e))


def run_panel_parser_consumer():
    """Start the Panel Parser Consumer"""
    try:
        logger.info("Starting Panel Parser Consumer")
        consumer = PanelParserConsumer()
        consumer.start_consuming()
    except Exception as e:
        logger.error("Error running Panel parser consumer", error=str(e))


def run_panel_dispatcher_consumer():
    """Start the PANEL Dispatcher Consumer"""
    try:
        logger.info("Starting PANEL Dispatcher Consumer")
        consumer = PanelDispatcherConsumer()
        consumer.start_consuming()
    except Exception as e:
        logger.error("Error running PANEL dispatcher consumer", error=str(e))

def run_report_parser_consumer():
    """Start the Report Parser Consumer"""
    try:
        logger.info("Starting Report Parser Consumer")
        consumer = ReportParserConsumer()
        consumer.start_consuming()
    except Exception as e:
        logger.error("Error running Report parser consumer", error=str(e))


def run_report_dispatcher_consumer():
    """Start the REPORT Dispatcher Consumer"""
    try:
        logger.info("Starting REPORT Dispatcher Consumer")
        consumer = ReportDispatcherConsumer()
        consumer.start_consuming()
    except Exception as e:
        logger.error("Error running REPORT dispatcher consumer", error=str(e))
def run_copybook_dnp_consumer():
    """Start the DNP Copybook Parser Consumer"""
    try:
        logger.info("Starting DNP Copybook Parser Consumer")
        consumer = CopybookDNPParserConsumer()
        consumer.start_consuming()
    except Exception as e:
        logger.error("Error running consumer", error=str(e))


def run_copybook_unisys_consumer():
    """Start the Unisys Copybook Parser Consumer"""
    try:
        logger.info("Starting Unisys Copybook Parser Consumer")
        consumer = CopybookUnisysParserConsumer()
        consumer.start_consuming()
    except Exception as e:
        logger.error("Error running consumer", error=str(e))


def run_email_consumer():
    """Start the Email Consumer"""
    try:
        logger.info("Starting Email Consumer")
        consumer = EmailConsumer()
        consumer.start_consuming()
    except Exception as e:
        logger.error("Error running consumer", error=str(e))


def run_cobol_unisys_consumer():
    """Start the Unisys Cobol Parser Consumer"""
    try:
        logger.info("Starting Unisys Cobol Parser Consumer")
        consumer = CobolUnisysParserConsumer()
        consumer.start_consuming()
    except Exception as e:
        logger.error("Error running consumer", error=str(e))


def run_cobol_dnp_consumer():
    """Start the DNP Cobol Parser Consumer"""
    try:
        logger.info("Starting DNP Cobol Parser Consumer")
        consumer = CobolDNPParserConsumer()
        consumer.start_consuming()
    except Exception as e:
        logger.error("Error running consumer", error=str(e))

def run_bat_consumer():
    """Start the Batch Parser Consumer"""
    try:
        logger.info("Starting Batch Parser Consumer")
        consumer = BatchParserConsumer()
        consumer.start_consuming()
    except Exception as e:
        logger.error("Error running consumer", error=str(e))

def run_cobol_dispatcher_consumer():
    """Start the Cobol Dispatcher Consumer"""
    try:
        logger.info("Starting Cobol Dispatcher Consumer")
        consumer = CobolDispatcherConsumer()
        consumer.start_consuming()
    except Exception as e:
        logger.error("Error running consumer", error=str(e))


def run_wfl_dispatcher_consumer():
    """Start the WFL Dispatcher Consumer"""
    try:
        logger.info("Starting WFL Dispatcher Consumer")
        consumer = WFLDispatcherConsumer()
        consumer.start_consuming()
    except Exception as e:
        logger.error("Error running consumer", error=str(e))


def run_graph_consumer():
    """Start the Graph Consumer"""
    try:
        logger.info("Start the DNP Graph Consumer")
        consumer = GraphConsumer()
        consumer.start_consuming()
    except Exception as e:
        logger.error("Error running consumer", error=str(e))


def run_cobol_summarization_consumer():
    """Start the Cobol Summarization Consumer"""
    try:
        logger.info("Starting Cobol Summarization Consumer")
        consumer = CobolSummarizationConsumer()
        consumer.start_consuming()
    except Exception as e:
        logger.error("Error running consumer", error=str(e))


def run_bms_summarization_consumer():
    """Start the BMS Summarization Consumer"""
    try:
        logger.info("Starting BMS Summarization Consumer")
        consumer = BMSSummarizationConsumer()
        consumer.start_consuming()
    except Exception as e:
        logger.error("Error running consumer", error=str(e))


def run_cobol_screen_summarization_consumer():
    """Start the COBOL Screen Summarization Consumer"""
    try:
        logger.info("Starting COBOL Screen Summarization Consumer")
        consumer = CobolScreenSummarizationConsumer()
        consumer.start_consuming()
    except Exception as e:
        logger.error("Error running consumer", error=str(e))


def run_cobol_java_migration_consumer():
    """Start the COBOL JAVA Migration Consumer"""
    try:
        logger.info("Starting COBOL JAVA Migration Consumer")
        consumer = CobolJavaMigrationConsumer()
        consumer.start_consuming()
    except Exception as e:
        logger.error("Error running consumer", error=str(e))


def run_bms_java_migration_consumer():
    """Start the BMS JAVA Migration Consumer"""
    try:
        logger.info("Starting BMS JAVA Migration Consumer")
        consumer = BMSJavaMigrationConsumer()
        consumer.start_consuming()
    except Exception as e:
        logger.error("Error running consumer", error=str(e))


def run_assessment_consumer():
    """Start the Assessment Consumer"""
    try:
        logger.info("Start the Assessment Consumer")
        consumer = AssessmentConsumer()
        consumer.start_consuming()
    except Exception as e:
        logger.error("Error running consumer", error=str(e))


def run_statement_summarization_consumer():
    """Start the Statement Summarization Consumer"""
    try:
        logger.info("Starting Statement Summarization Consumer")
        consumer = StatementSummarizationConsumer()
        consumer.start_consuming()
    except Exception as e:
        logger.error("Error running consumer", error=str(e))


def run_wfl_consumer():
    """Start the WFL Parser Consumer"""
    try:
        logger.info("Starting WFL Parser Consumer")
        consumer = WFLParserConsumer()
        consumer.start_consuming()
    except Exception as e:
        logger.error("Error running consumer", error=str(e))


def run_bms_modernization_consumer():
    """Start the BMS Modernization Consumer"""
    try:
        logger.info("Starting BMS Modernization Consumer")
        consumer = BMSModernizationConsumer()
        consumer.start_consuming()
    except Exception as e:
        logger.error("Error running consumer", error=str(e))



def run_copybook_summarization_consumer():
    """Start the Copybook Summarization Consumer"""
    try:
        logger.info("Starting Copybook Summarization Consumer")
        consumer = CopybookSummarizationConsumer()
        consumer.start_consuming()
    except Exception as e:
        logger.error("Error running consumer", error=str(e))


def run_all_consumers():
    """Start all Consumers"""
    consumers = [
        # run_cobol_dispatcher_consumer,
        # run_bat_consumer,
        # run_wfl_dispatcher_consumer,
        # run_cobol_unisys_consumer,
        # run_cobol_dnp_consumer,
        # run_copybook_dnp_consumer,
        # run_assessment_consumer,
        # run_copybook_unisys_consumer,
        # run_graph_consumer,
        run_cobol_summarization_consumer,
        run_statement_summarization_consumer,
        # run_wfl_consumer,
        run_bms_modernization_consumer,
        # run_clist_parser_consumer,
        # run_clist_dispatcher_consumer,
        # run_panel_parser_consumer,
        # run_panel_dispatcher_consumer,
        # run_report_parser_consumer,
        # run_report_dispatcher_consumer,
        # run_bms_java_migration_consumer,
        # run_cobol_java_migration_consumer,
        run_bms_summarization_consumer,
    ]
    processes_list = []
    for consumer in consumers:
        p = Process(target=consumer)
        p.start()
        processes_list.append(p)
        logger.info(f"Started {consumer.__name__} process")

    for p in processes_list:
        p.join()


@click.group()
def cli():
    pass


@cli.command()
@click.option('--processes', '-p', default=1, help='Number of consumer processes')
def assessment(processes):
    """Start Assessment Consumers"""
    processes_list = []
    for i in range(processes):
        p = Process(target=run_assessment_consumer)
        p.start()
        processes_list.append(p)
        logger.info(f"Started Assessment Consumer process {i + 1}")

    for p in processes_list:
        p.join()


@cli.command()
@click.option('--processes', '-p', default=1, help='Number of consumer processes')
def copybookdnp(processes):
    """Start DNP Copybook Parser Consumers"""
    processes_list = []
    for i in range(processes):
        p = Process(target=run_copybook_dnp_consumer)
        p.start()
        processes_list.append(p)
        logger.info(f"Started DNP Copybook Parser Consumer process {i + 1}")

    for p in processes_list:
        p.join()


@cli.command()
@click.option('--processes', '-p', default=1, help='Number of consumer processes')
def copybookunisys(processes):
    """Start Copybook Unisys Parser Consumers"""
    processes_list = []
    for i in range(processes):
        p = Process(target=run_copybook_unisys_consumer)
        p.start()
        processes_list.append(p)
        logger.info(f"Started Copybook Unisys Parser Consumer process {i + 1}")

    for p in processes_list:
        p.join()


@cli.command()
@click.option('--processes', '-p', default=1, help='Number of consumer processes')
def copybookunisys(processes):
    """Start Copybook Unisys Parser Consumers"""
    processes_list = []
    for i in range(processes):
        p = Process(target=run_copybook_unisys_consumer)
        p.start()
        processes_list.append(p)
        logger.info(f"Started Copybook Unisys Parser Consumer process {i + 1}")

    for p in processes_list:
        p.join()


@cli.command()
@click.option('--processes', '-p', default=1, help='Number of consumer processes')
def email(processes):
    """Start Email Consumers"""
    processes_list = []
    for i in range(processes):
        p = Process(target=run_email_consumer)
        p.start()
        processes_list.append(p)
        logger.info(f"Started Email Consumer process {i + 1}")

    for p in processes_list:
        p.join()


@cli.command()
@click.option('--processes', '-p', default=1, help='Number of consumer processes')
def cobolunisys(processes):
    """Start Cobol Unisys Parser Consumers"""
    processes_list = []
    for i in range(processes):
        p = Process(target=run_cobol_unisys_consumer)
        p.start()
        processes_list.append(p)
        logger.info(f"Started Cobol Unisys Parser Consumer process {i + 1}")

    for p in processes_list:
        p.join()


@cli.command()
@click.option('--processes', '-p', default=1, help='Number of consumer processes')
def coboldnp(processes):
    """Start Cobol DNP Parser Consumers"""
    processes_list = []
    for i in range(processes):
        p = Process(target=run_cobol_dnp_consumer)
        p.start()
        processes_list.append(p)
        logger.info(f"Started Cobol DNP Parser Consumer process {i + 1}")

    for p in processes_list:
        p.join()


@cli.command()
@click.option('--processes', '-p', default=1, help='Number of consumer processes')
def coboldispatcher(processes):
    """Start Cobol Dispatcher Consumers"""
    processes_list = []
    for i in range(processes):
        p = Process(target=run_cobol_dispatcher_consumer)
        p.start()
        processes_list.append(p)
        logger.info(f"Started Cobol Dispatcher Consumer process {i + 1}")

    for p in processes_list:
        p.join()


@cli.command()
@click.option('--processes', '-p', default=1, help='Number of consumer processes')
def bat(processes):
    """Start Batch Parser Consumers"""
    processes_list = []
    for i in range(processes):
        p = Process(target=run_bat_consumer)
        p.start()
        processes_list.append(p)
        logger.info(f"Started BMS Parser Consumer process {i + 1}")

    for p in processes_list:
        p.join()



@cli.command()
@click.option('--processes', '-p', default=1, help='Number of consumer processes')
def wfldispatcher(processes):
    """Start WFL Dispatcher Consumers"""
    processes_list = []
    for i in range(processes):
        p = Process(target=run_wfl_dispatcher_consumer)
        p.start()
        processes_list.append(p)
        logger.info(f"Started WFL Dispatcher Consumer process {i + 1}")

    for p in processes_list:
        p.join()


@cli.command()
@click.option('--processes', '-p', default=1, help='Number of consumer processes')
def graph(processes):
    """Start Graph Consumers"""
    processes_list = []
    for i in range(processes):
        p = Process(target=run_graph_consumer)
        p.start()
        processes_list.append(p)
    logger.info(f"Started Graph Consumer process {i + 1}")
    for p in processes_list:
        p.join()


@cli.command()
@click.option('--processes', '-p', default=1, help='Number of consumer processes')
def cobolsummarization(processes):
    """Start COBOL Summarization Consumers"""
    processes_list = []
    for i in range(processes):
        p = Process(target=run_cobol_summarization_consumer)
        p.start()
        processes_list.append(p)
        logger.info(f"Started cobol_summarization_consumer process {i + 1}")
    for p in processes_list:
        p.join()


@cli.command()
@click.option('--processes', '-p', default=1, help='Number of consumer processes')
def cobolmigration(processes):
    """Start COBOL Migration Consumers"""
    processes_list = []
    for i in range(processes):
        p = Process(target=run_cobol_java_migration_consumer())
        p.start()
        processes_list.append(p)
        logger.info(f"Started cobol_java_migration_consumer process {i + 1}")
    for p in processes_list:
        p.join()


@cli.command()
@click.option('--processes', '-p', default=1, help='Number of consumer processes')
def bmsmigration(processes):
    """Start BMS Migration Consumers"""
    processes_list = []
    for i in range(processes):
        p = Process(target=run_bms_java_migration_consumer())
        p.start()
        processes_list.append(p)
        logger.info(f"Started bms_java_migration_consumer process {i + 1}")
    for p in processes_list:
        p.join()


@cli.command()
@click.option('--processes', '-p', default=1, help='Number of consumer processes')
def bmssummarization(processes):
    """Start BMS Summarization Consumers"""
    processes_list = []
    for i in range(processes):
        p = Process(target=run_bms_summarization_consumer())
        p.start()
        processes_list.append(p)
        logger.info(f"Started bms_summarization_consumer process {i + 1}")
    for p in processes_list:
        p.join()


@cli.command()
@click.option('--processes', '-p', default=1, help='Number of consumer processes')
def statementsummarization(processes):
    """Start Statement Summarization Consumers"""
    processes_list = []
    for i in range(processes):
        p = Process(target=run_statement_summarization_consumer)
        p.start()
        processes_list.append(p)
        logger.info(f"Started Statement Summarization Consumer process {i + 1}")

    for p in processes_list:
        p.join()


@cli.command()
@click.option('--processes', '-p', default=1, help='Number of consumer processes')
def wfl(processes):
    """Start WFL Parser Consumers"""
    processes_list = []
    for i in range(processes):
        p = Process(target=run_wfl_consumer)
        p.start()
        processes_list.append(p)
        logger.info(f"Started WFL Parser Consumer process {i + 1}")

    for p in processes_list:
        p.join()


@cli.command()
@click.option('--processes', '-p', default=1, help='Number of consumer processes')
def bmsmodernization(processes):
    """Start BMS Modernization Consumers"""
    processes_list = []
    for i in range(processes):
        p = Process(target=run_bms_modernization_consumer)
        p.start()
        processes_list.append(p)
        logger.info(f"Started BMS Modernization Consumer process {i + 1}")

    for p in processes_list:
        p.join()


@cli.command()
@click.option('--processes', '-p', default=1, help='Number of consumer processes')
def all(processes):
    """Start all Consumers"""
    processes_list = []
    for i in range(processes):
        p = Process(target=run_all_consumers)
        p.start()
        processes_list.append(p)
        logger.info(f"Started all consumers process {i + 1}")

    for p in processes_list:
        p.join()


if __name__ == "__main__":
    cli()
