import TrendingUpIcon from '@mui/icons-material/TrendingUp';
import { Box, Stack, Typography } from '@mui/material';

import type { KpiMetric } from '../types/dashboard';
import { DashboardCard } from './DashboardCard';

type KpiCardProps = {
  metric: KpiMetric;
};

export function KpiCard({ metric }: KpiCardProps) {
  return (
    <DashboardCard aria-label={`${metric.label}: ${metric.value}`}>
      <Stack spacing={2}>
        <Stack direction="row" sx={{ justifyContent: 'space-between', alignItems: 'center' }}>
          <Typography variant="body2" color="text.secondary" sx={{ fontWeight: 700 }}>
            {metric.label}
          </Typography>
          <Box sx={{ color: 'success.main', display: 'grid', placeItems: 'center' }}>
            <TrendingUpIcon fontSize="small" />
          </Box>
        </Stack>
        <Box>
          <Typography variant="h4" component="p">
            {metric.value}
          </Typography>
          <Typography variant="body2" color="text.secondary" sx={{ mt: 0.5 }}>
            {metric.helper}
          </Typography>
        </Box>
      </Stack>
    </DashboardCard>
  );
}
