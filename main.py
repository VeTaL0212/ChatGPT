import g4f
import asyncio

_providers = g4f.Provider.ChatBase
    # g4f.Provider.ChatBase,
    # g4f.Provider.Aura,
    # g4f.Provider.DeepInfa,
    # g4f.Provider.HuggintChat,
    # g4f.Provider.Pi,


async def run_provider(provider: g4f.Provider.BaseProvider):
    try:
        response = await g4f.ChatCompletion.create_async(
            model=g4f.models.default,
            messages=[{"role": "user", "content": "Кто ты такой?"}],
            provider=provider,
        )
        print(f"{provider.__name__}:", response)
    except Exception as e:
        print(f"{provider.__name__}:", e)

async def run_all():
    calls = [
        run_provider(provider) for provider in _providers
    ]
    await asyncio.gather(*calls)


asyncio.run(run_all())