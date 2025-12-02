# Setting up Kitsu for Prism with a self-hosted QNAP NAS

These steps walk through installing the Prism Kitsu plugin and connecting it to a Kitsu instance hosted on a QNAP NAS. The goal is to sync projects, tasks, and publishes between Prism and Kitsu while keeping naming and versioning consistent.

## Prerequisites
- Prism installed on your workstation (Windows, Linux, or macOS).
- A running Kitsu instance on your QNAP NAS with a reachable URL (e.g. `https://nas.example.com/kitsu`).
- A Kitsu account with permissions to create projects, tasks, and publishes.
- Network access from your workstation to the NAS (HTTP/HTTPS and any reverse-proxy ports).

## Install the plugin
1. Download or clone this repository.
2. Rename the root folder to **`Kitsu`**.
3. Copy the folder to your Prism installation at `Prism/Plugins/ProjectManagers/Kitsu/` so that the `Scripts/` and `external_modules/` folders sit directly inside the `Kitsu` folder.
4. Restart Prism and any open DCC applications.

## Configure Kitsu access
1. Open **Prism Settings → Project Managers → Kitsu**.
2. Enter the Kitsu credentials that Prism should use:
   - **Username** and **Password**: Use a service account that has access to your productions on the NAS.
3. Under **Kitsu integration**:
   - Enable the checkbox to activate the plugin.
   - **Kitsu site**: Enter the full URL to your NAS-hosted Kitsu (e.g. `https://nas.example.com/kitsu`). Avoid trailing slashes.
   - **Project Name**: Use the exact project name as it appears in Kitsu.
   - Toggle **Only sync user assigned tasks** if you want to limit the sync scope.
   - Toggle **Set first frame to 1** if your Kitsu shots only specify frame counts and you want Prism to start at frame 1.
4. Click **Check login** to validate connectivity. If the check fails, verify DNS, SSL certificates, and that the Kitsu reverse proxy on the NAS allows API access.

## Sync guidelines
- Use Prism's **Project Browser** to trigger syncs for assets and shots. The plugin will align descriptions, frame ranges, thumbnails, and publish statuses with Kitsu.
- Keep Kitsu task types aligned with your Prism steps. If you add new task types in Kitsu, create matching steps in Prism before syncing to avoid missing categories.
- For consistent naming/versioning, rely on Prism's save/publish templates. The plugin will use Prism's versioned publish paths when sending renders back to Kitsu.
- When working with image sequences, the plugin converts them to temporary movies for upload and removes the temp files after publishing.

## QNAP-specific considerations
- If the NAS is behind HTTPS with a self-signed certificate, add the certificate to your OS trust store so Python (and Qt) can validate the connection.
- Ensure the NAS firewall and reverse proxy expose the Kitsu API route (usually `/api`).
- Keep the NAS timezone synchronized with your workstations to prevent confusing timestamps on publishes and tasks.

## Troubleshooting
- **Plugin does not load**: Confirm the folder structure is exactly `Prism/Plugins/ProjectManagers/Kitsu/` with `Scripts/` and `external_modules/` inside.
- **Login fails**: Double-check the site URL, project name, and credentials. Try the same account directly in the Kitsu web UI.
- **Tasks do not appear**: Disable "Only sync user assigned tasks" to verify connectivity, then re-enable after confirming the sync works.
- **Slow uploads**: Large renders may take time to transcode on the workstation before uploading to the NAS. Consider keeping image sequences short or using lower-resolution previews for quick iterations.
