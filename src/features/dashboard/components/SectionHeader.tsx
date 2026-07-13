import { Stack, Typography } from '@mui/material';

type SectionHeaderProps = {
  eyebrow?: string;
  title: string;
  description?: string;
};

export function SectionHeader({ eyebrow, title, description }: SectionHeaderProps) {
  return (
    <Stack spacing={0.75} component="header">
      {eyebrow ? (
        <Typography variant="overline" color="secondary" sx={{ fontWeight: 800, letterSpacing: 1.2 }}>
          {eyebrow}
        </Typography>
      ) : null}
      <Typography variant="h5" component="h2">
        {title}
      </Typography>
      {description ? <Typography color="text.secondary">{description}</Typography> : null}
    </Stack>
  );
}
