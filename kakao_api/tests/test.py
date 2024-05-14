from kakao_api import KakaoApi
import asyncio

kakao = KakaoApi(
    client_id="<CLIENT_KEY>",
    admin_key="<ADMIN_KEY>",
)


async def main() -> None:
    users = await kakao.get_user_list()
    print(users.elements)
    res = await kakao.get_users_info(
        target_ids=users.elements
    )
    print(res)


asyncio.run(main())