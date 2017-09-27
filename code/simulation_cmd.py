from runner import Runner
import logging
import time
from postprocessing import PostProcessing
from event import Event
import config
from context import Context
from prepare import Prepare
from write import Writer
import utils


def run():
    for file in [config.ticks_csv, config.network_csv, config.nodes_csv]:
        utils.check_for_file(file)

    context = Context()
    context.create()

    logging.info(config.log_line_run_start + context.run_name)

    tag = context.args.tag
    if hasattr(context.args, 'tag_appendix'):
        tag += context.args.tag_appendix
    writer = Writer(tag)
    runner = Runner(context, writer)

    prepare = Prepare(context)
    runner.prepare = prepare

    postprocessing = PostProcessing(context, writer)
    runner.postprocessing = postprocessing

    event = Event(context)
    runner.event = event

    start = time.time()

    runner.run()

    logging.info("The duration of the run was {} seconds".format(str(time.time() - start)))
