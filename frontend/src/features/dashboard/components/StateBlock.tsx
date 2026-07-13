import WarningAmberIcon from '@mui/icons-material/WarningAmber';
import { Alert, Box, Button, Skeleton, Stack, Typography } from '@mui/material';

export function DashboardSkeleton() {
  return (
    <Stack spacing={3} aria-label="Loading AI workspace">
      <Skeleton variant="rounded" height={180} />
      <Stack direction={{ xs: 'column', md: 'row' }} spacing={2}>
        <Skeleton variant="rounded" height={160} sx={{ flex: 1 }} />
        <Skeleton variant="rounded" height={160} sx={{ flex: 1 }} />
        <Skeleton variant="rounded" height={160} sx={{ flex: 1 }} />
      </Stack>
      <Skeleton variant="rounded" height={320} />
    </Stack>
  );
}

type EmptyStateProps = {
  title: string;
  description: string;
};

export function EmptyState({ title, description }: EmptyStateProps) {
  return (
    <Box sx={{ border: '1px dashed', borderColor: 'divider', borderRadius: 4, p: 4, textAlign: 'center' }}>
      <Typography variant="h6">{title}</Typography>
      <Typography color="text.secondary" sx={{ mt: 1 }}>
        {description}
      </Typography>
    </Box>
  );
}

type ErrorStateProps = {
  onRetry: () => void;
};

export function ErrorState({ onRetry }: ErrorStateProps) {
  return (
    <Alert
      severity="error"
      icon={<WarningAmberIcon />}
      action={
        <Button color="inherit" size="small" onClick={onRetry}>
          Retry
        </Button>
      }
    >
      We could not load today&apos;s AI workspace. Please try refreshing the briefing.
    </Alert>
  );
}
