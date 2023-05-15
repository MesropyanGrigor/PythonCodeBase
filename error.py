def error_handler(func: Callable[..., Any]) -> Callable[..., Any]:
    def decorator(self: Any, *args: tuple[Any], **kwargs: Mapping[str, str]) -> Any:
        try:
            return func(
                self,
                *args,
                **kwargs,
            )
        except currencycloud.errors.api.ApiError as exc:
            errors = []
            for message in exc.messages:
                _logger.error(
                    message.message,
                    provider="Currency Cloud",
                    method=func.__name__,
                )
                errors.append(message.message)

            raise CurrencyCloudError(
                errors,
                status=exc.status_code,
            ) from exc

    return decorator
