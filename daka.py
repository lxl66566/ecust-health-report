from playwright.async_api import Playwright, async_playwright
from playwright._impl._api_types import TimeoutError as Terror
import asyncio

async def mina():
    account = '********'
    password = '***********'
    try:
        async with async_playwright() as playwright:
            await run(playwright, account, password)
    except Terror:
        msg = '健康打卡失败，可能已自行打卡，请注意需自行填写'
    except Exception as e:
        msg = f'健康打卡失败 错误原因{e}'
    else:
        msg = '今日已完成健康打卡'
    print(msg)
    
async def run(playwright: Playwright, stu_id, password) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    # Open new page
    page = await context.new_page()
    await page.goto(
        "https://sso.ecust.edu.cn/authserver/login?service=https%3A%2F%2Fworkflow.ecust.edu.cn%2Fdefault%2Fwork%2Fuust%2Fzxxsmryb%2Fmrybcn.jsp")
    # Click [placeholder="用户名"]
    await page.click("[placeholder=\"用户名\"]")
    # Fill [placeholder="用户名"]
    await page.fill("[placeholder=\"用户名\"]", stu_id)
    # Click [placeholder="密码"]
    await page.click("[placeholder=\"密码\"]")
    # Fill [placeholder="密码"]
    await page.fill("[placeholder=\"密码\"]", password)
    # Click button:has-text("登录")
    await page.click("button:has-text(\"登录\")")
    # assert page.url == "https://workflow.ecust.edu.cn/default/work/uust/zxxsmryb/mrybcn.jsp"
    # Click ins
    await page.click("ins")
    # Click text=下一步
    await page.click("text=下一步")
    await page.click("label:has-text(\"健康\")")
    # Click #radio_sfycxxwc42
    await page.click("#radio_sfycxxwc42")
    # Click text=*行程码是否绿码： 是否 >> ins
    await page.click("#radio_xcm5")
    await page.click("text=在上海")
    # Click text=提交
    await page.click("text=提交")
    # Click text=确定
    await page.click("text=确定")
    # Click text=确定
    await page.click("text=确定")
    # ---------------------
    await context.close()
    await browser.close()

loop = asyncio.get_event_loop()
task = [asyncio.ensure_future(mina())]
loop.run_until_complete(asyncio.wait(task))
loop.close()
