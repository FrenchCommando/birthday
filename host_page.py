from aiohttp import web
import aiohttp_jinja2
import jinja2
from pathlib import Path
from gmail.gmail_main import main


router = web.RouteTableDef()


@router.get('/')
async def greet_user(request: web.Request) -> web.Response:
    context = {
        "username": "My Darling",
    }
    response = aiohttp_jinja2.render_template(
        "base.html",
        request,
        context=context
    )
    return response


@router.get('/present')
async def show_present(request: web.Request) -> web.Response:
    context = {}
    main()
    response = aiohttp_jinja2.render_template(
        "target.html",
        request,
        context=context
    )
    return response


async def init_app() -> web.Application:
    app = web.Application()
    app.add_routes(router)
    aiohttp_jinja2.setup(
        app, loader=jinja2.FileSystemLoader(str(Path(__file__).parent / "templates"))
    )
    return app


web.run_app(init_app(), port="8888")
