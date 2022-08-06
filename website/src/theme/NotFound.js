import React from 'react';
import {translate} from '@docusaurus/Translate';
import {PageMetadata} from '@docusaurus/theme-common';
import Layout from '@theme/Layout';
import Link from "@docusaurus/Link";

export default function NotFound() {
    return (
        <>
            <PageMetadata
                title={translate({
                    id: 'theme.NotFound.title',
                    message: 'Page Not Found',
                })}
            />
            <Layout>
                <main className="container margin-vert--xl">
                    <div className="row">
                        <div className="col col--6 col--offset-3">
                            <h1 className="hero__title">
                                Page Not Found
                            </h1>
                            <p>
                                I don't even know how that's possible.
                            </p>
                            <p>
                                If you are absolutely confident that you are here by no mistake of your own, please
                                <Link to="https://github.com/celsiusnarhwal/vercel-badge/issues"> open an issue on
                                    GitHub.</Link>
                            </p>
                        </div>
                    </div>
                </main>
            </Layout>
        </>
    );
}
