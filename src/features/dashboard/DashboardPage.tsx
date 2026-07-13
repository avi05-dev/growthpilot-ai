import AutoAwesomeIcon from '@mui/icons-material/AutoAwesome';
import CalendarMonthIcon from '@mui/icons-material/CalendarMonth';
import EditNoteIcon from '@mui/icons-material/EditNote';
import { Box, Button, Chip, Grid, Stack, Typography } from '@mui/material';
import { useCallback, useEffect, useMemo, useState } from 'react';

import { ActionItem } from './components/ActionItem';
import { DashboardCard } from './components/DashboardCard';
import { DashboardSkeleton, EmptyState, ErrorState } from './components/StateBlock';
import { HeroHeader } from './components/HeroHeader';
import { KpiCard } from './components/KpiCard';
import { SectionHeader } from './components/SectionHeader';
import { TrendCard } from './components/TrendCard';
import { getDashboardData } from './services/mockDashboardService';
import type { DashboardData, DashboardLoadState, TrendCategory } from './types/dashboard';

const trendCategories: TrendCategory[] = ['AI', 'Development', 'Career'];

export function DashboardPage() {
  const [dashboardData, setDashboardData] = useState<DashboardData | null>(null);
  const [loadState, setLoadState] = useState<DashboardLoadState>('loading');

  const loadDashboard = useCallback(async () => {
    setLoadState('loading');

    try {
      const data = await getDashboardData();
      setDashboardData(data);
      setLoadState(data.trends.length === 0 ? 'empty' : 'success');
    } catch {
      setLoadState('error');
    }
  }, []);

  useEffect(() => {
    void loadDashboard();
  }, [loadDashboard]);

  const trendsByCategory = useMemo(() => {
    return trendCategories.map((category) => ({
      category,
      trends: dashboardData?.trends.filter((trend) => trend.category === category) ?? [],
    }));
  }, [dashboardData]);

  return (
    <Stack spacing={{ xs: 3, md: 4 }}>
      <HeroHeader onRefresh={loadDashboard} />

      {loadState === 'loading' ? <DashboardSkeleton /> : null}
      {loadState === 'error' ? <ErrorState onRetry={loadDashboard} /> : null}
      {loadState === 'empty' ? <EmptyState title="No growth signals yet" description="Your workspace is ready, but there are no mock trends to display." /> : null}

      {loadState === 'success' && dashboardData ? (
        <Stack spacing={{ xs: 3, md: 4 }}>
          <Grid container spacing={3} alignItems="stretch">
            <Grid item xs={12} lg={7}>
              <DashboardCard>
                <Stack spacing={3}>
                  <SectionHeader eyebrow="AI Daily Briefing" title={dashboardData.briefing.title} description="A concise operating brief for deciding what to do today." />
                  <Stack component="ul" spacing={1.5} sx={{ pl: 0, m: 0 }}>
                    {dashboardData.briefing.items.map((item) => (
                      <Stack key={item.id} component="li" direction="row" spacing={1.5} sx={{ listStyle: 'none' }}>
                        <AutoAwesomeIcon color="secondary" fontSize="small" />
                        <Typography>{item.text}</Typography>
                      </Stack>
                    ))}
                  </Stack>
                  <Box sx={{ border: '1px solid', borderColor: 'divider', borderRadius: 3, p: 2.5, bgcolor: 'background.default' }}>
                    <Stack direction={{ xs: 'column', sm: 'row' }} spacing={2} justifyContent="space-between">
                      <Box>
                        <Typography variant="body2" color="text.secondary" fontWeight={800}>
                          Best posting window
                        </Typography>
                        <Typography variant="h6" sx={{ mt: 0.5 }}>
                          {dashboardData.briefing.bestPostingWindow}
                        </Typography>
                      </Box>
                      <CalendarMonthIcon color="secondary" aria-hidden="true" />
                    </Stack>
                  </Box>
                  <Box>
                    <Typography variant="body2" color="text.secondary" fontWeight={800}>
                      Recommended Focus
                    </Typography>
                    <Typography variant="h6" component="p" sx={{ mt: 0.75 }}>
                      {dashboardData.briefing.recommendedFocus}
                    </Typography>
                  </Box>
                </Stack>
              </DashboardCard>
            </Grid>

            <Grid item xs={12} lg={5}>
              <DashboardCard>
                <Stack spacing={3}>
                  <SectionHeader eyebrow="Content Studio" title="Preview" description="Draft recommendations prepared from today's strongest signals." />
                  <Stack spacing={2}>
                    {dashboardData.contentRecommendations.map((recommendation) => (
                      <Box key={recommendation.id} sx={{ border: '1px solid', borderColor: 'divider', borderRadius: 3, p: 2 }}>
                        <Stack direction="row" justifyContent="space-between" alignItems="flex-start" gap={2}>
                          <Box>
                            <Chip label={recommendation.channel} size="small" variant="outlined" />
                            <Typography variant="h6" component="h3" sx={{ mt: 1 }}>
                              {recommendation.topic}
                            </Typography>
                          </Box>
                          <Button variant="contained" size="small" startIcon={<EditNoteIcon />} aria-label={`${recommendation.actionLabel} for ${recommendation.topic}`}>
                            {recommendation.actionLabel}
                          </Button>
                        </Stack>
                      </Box>
                    ))}
                  </Stack>
                </Stack>
              </DashboardCard>
            </Grid>
          </Grid>

          <Box component="section" aria-labelledby="trend-radar-heading">
            <SectionHeader eyebrow="Trend Radar" title="Signals to turn into content" description="Mock source badges show where each trend would be validated when live integrations arrive." />
            <Stack spacing={3} sx={{ mt: 3 }}>
              {trendsByCategory.map(({ category, trends }) => (
                <Box key={category}>
                  <Typography id={category === 'AI' ? 'trend-radar-heading' : undefined} variant="h6" component="h3" sx={{ mb: 2 }}>
                    {category}
                  </Typography>
                  <Grid container spacing={2.5}>
                    {trends.map((trend) => (
                      <Grid key={trend.id} item xs={12} md={6} xl={4}>
                        <TrendCard trend={trend} />
                      </Grid>
                    ))}
                  </Grid>
                </Box>
              ))}
            </Stack>
          </Box>

          <Grid container spacing={3} alignItems="stretch">
            <Grid item xs={12} lg={6}>
              <DashboardCard>
                <Stack spacing={3}>
                  <SectionHeader eyebrow="Action Center" title="What should I do today?" description="A prioritized plan for learning, creating, and publishing." />
                  <Stack component="ul" spacing={1.5} sx={{ p: 0, m: 0 }}>
                    {dashboardData.actionTasks.map((task) => (
                      <ActionItem key={task.id} task={task} />
                    ))}
                  </Stack>
                </Stack>
              </DashboardCard>
            </Grid>
            <Grid item xs={12} lg={6}>
              <Stack spacing={3}>
                <SectionHeader eyebrow="Growth Snapshot" title="This week's momentum" description="Reusable KPI cards prepared for future analytics APIs." />
                <Grid container spacing={2.5}>
                  {dashboardData.kpis.map((metric) => (
                    <Grid key={metric.id} item xs={12} sm={6}>
                      <KpiCard metric={metric} />
                    </Grid>
                  ))}
                </Grid>
              </Stack>
            </Grid>
          </Grid>
        </Stack>
      ) : null}
    </Stack>
  );
}
