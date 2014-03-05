from buildbot.schedulers.forcesched import *
from buildbot_codeparameter import CodeParameter
demo1 = ForceScheduler(
    name="demo",
    label="Title for the Demo ForceScheduler",
    username=FixedParameter(name="username"),
    reason=FixedParameter(name="reason"),
    codebases = [CodebaseParameter("codebase", branch="",revision="",repository="",project="")],
    builderNames=["runtests1"],
    properties = [
        ParameterGroup(name='tabs', layout="tabs", fields=[
            ParameterGroup(name="demo", label="", tablabel='Form Demo', layout="vertical", fields=[
                ParameterGroup(label='Base Params', name="base", columns=3, fields=[
                    StringParameter(name="text", regexp="IWantToCreateABuild"),
                    IntParameter(name="int"),
                    FixedParameter(name="fixed"),
                    ChoiceStringParameter(name="list", choices=["v1", "v2"], default="v1"),
                    ChoiceStringParameter(name="list2", multiple=True, choices=["v3", "v4"]),
                    ]),
                ParameterGroup(label='Advanced Params', name="advanced", columns=1, fields=[
                    BooleanParameter(name="bool", default=True),
                    TextParameter(name="textarea", rows=4)
                    ]),
                ]),
            ParameterGroup(name="democode", label="", tablabel='Source Code', columns=1, fields=[
                CodeParameter(
                    name="code", height=400, mode="python", readonly=True,
                    default=open(__file__.rstrip("c")).read())
                ])
            ])
    ])
