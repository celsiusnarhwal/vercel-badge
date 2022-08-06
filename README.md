# Vercel Status Badge

Display the status of your [Vercel](https://vercel.com) deployment right in your repository's README.

## Badges

![Vercel](https://vercel.celsiusnarhwal.dev/api/ready) ![Vercel](https://vercel.celsiusnarhwal.dev/api/building)
![Vercel](https://vercel.celsiusnarhwal.dev/api/error) ![Vercel](https://vercel.celsiusnarhwal.dev/api/canceled)

## Usage

1. [Install the Vercel Status Badge app](https://vercel.celsiusnarhwal.dev). The app must have access to the
   repositories
   you want to display the badge on. If you select the "All repositories" option, you will never have to worry about
   this
   again.
2. Copy and paste one of following into your README.md, substituting `{user}` and `{repo}` with the appropriate values:
    - Markdown: `![Vercel](https://vercel.celsiusnarhwal.dev/api/{user}/{repo})`
    - HTML: `<img src="https://vercel.celsiusnarhwal.dev/api/{user}/{repo}"/>`

## Troubleshooting

**Q: I don't even see a badge, just some weird question mark thing. Please help.**

- Make sure the app is is installed on the repository you're trying to display the badge on.
- Make sure your badge URL is in the format `https://vercel.celsiusnarhwal.dev/api/{user}/{repo}`.
    - In particular, be sure that `celsiusnarhwal.dev` is spelled *exactly* as it appears here.
- Double-check your badge URL to see that the names of the repository and its owner are spelled correctly.
- [Uninstall](https://github.com/settings/installations), then [reinstall](https://vercel.celsiusnarhwal.dev/install),
  the app.
- Make sure the issue isn't your browser having cached an older version of the badge.
    - Clear your browser's cache.
    - View your repository in your browser's private browsing mode.
    - View your repository in a different browser.
- If it's still not working, [open an issue](/issues/new). Please include a link to the relevant repository.

**Q: I see a badge, but it doesn't line up with my deployment status on Vercel. Please help.**

- Make sure the deployment in question was deployed from your GitHub repository rather than another Git provider or
  the Vercel CLI. The badge API asks GitHub for the most recent deployment on your repository that was created by
  Vercel;
  it does not talk to Vercel directly. If your deployment was made from somewhere other than GitHub, things won't work.
- Make sure the issue isn't your browser having cached an older version of the badge.
    - Clear your browser's cache.
    - View your repository in your browser's private browsing mode.
    - View your repository in a different browser.
- Wait. GitHub limits how often the app can request your repo's deployment status. Give it an hour and see if the badge
  still isn't up-to-date.
- If it's still not working, [open an issue](/issues/new). Please include a link to the relevant repository.

## Acknowledgements

This project was inspired by [datejer/vercel-badge](https://github.com/datejer/vercel-badge).

Vercel, the Vercel design, Next.js and related marks, designs and logos are trademarks or registered trademarks of
Vercel, Inc. or its affiliates in the US and other countries.

## License

vercel-badge is licensed under the [MIT License](/LICENSE.md).
