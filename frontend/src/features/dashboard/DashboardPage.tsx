import AutoAwesomeIcon from '@mui/icons-material/AutoAwesome';
import CalendarMonthIcon from '@mui/icons-material/CalendarMonth';
import EditNoteIcon from '@mui/icons-material/EditNote';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import { Accordion, AccordionDetails, AccordionSummary, Box, Button, Chip, Grid, LinearProgress, Stack, Tooltip, Typography } from '@mui/material';
import { useQuery } from '@tanstack/react-query';

import { DashboardApi } from '../../api/dashboardApi';
import { KnowledgeApi } from '../../api/knowledgeApi';
import { RecommendationApi } from '../../api/recommendationApi';
import { TrendApi } from '../../api/trendApi';
import { ActionItem } from './components/ActionItem';
import { DashboardCard } from './components/DashboardCard';
import { DashboardSkeleton, EmptyState, ErrorState } from './components/StateBlock';
import { HeroHeader } from './components/HeroHeader';
import { KpiCard } from './components/KpiCard';
import { SectionHeader } from './components/SectionHeader';
import { TrendCard } from './components/TrendCard';
import type { TrendCategory } from './types/dashboard';

const trendCategories: TrendCategory[] = ['AI', 'Development', 'Career'];

export function DashboardPage() {
  const dashboardQuery = useQuery({ queryKey: ['dashboard'], queryFn: DashboardApi.getDashboard });
  const trendsQuery = useQuery({ queryKey: ['trends'], queryFn: TrendApi.getTrends });
  const recommendationsQuery = useQuery({ queryKey: ['recommendations'], queryFn: RecommendationApi.getRecommendations });
  const knowledgeQuery = useQuery({ queryKey: ['knowledge'], queryFn: KnowledgeApi.getKnowledge });

  const isLoading = dashboardQuery.isLoading || trendsQuery.isLoading || recommendationsQuery.isLoading || knowledgeQuery.isLoading;
  const isError = dashboardQuery.isError || trendsQuery.isError || recommendationsQuery.isError || knowledgeQuery.isError;

  const refreshDashboard = () => {
    void dashboardQuery.refetch();
    void trendsQuery.refetch();
    void recommendationsQuery.refetch();
    void knowledgeQuery.refetch();
  };

  const trends = trendsQuery.data?.trends ?? [];
  const recommendations = recommendationsQuery.data?.recommendations ?? [];
  const knowledgeItems = knowledgeQuery.data?.knowledge ?? [];
  const dashboardData = dashboardQuery.data;

  const trendsByCategory = trendCategories.map((category) => ({
    category,
    trends: trends.filter((trend) => trend.category === category),
  }));

  const hasNoData = trends.length === 0 && recommendations.length === 0 && knowledgeItems.length === 0 && dashboardData?.actionTasks.length === 0;

  return (
    <Stack spacing={{ xs: 3, md: 4 }}>
      <HeroHeader onRefresh={refreshDashboard} />

      {isLoading ? <DashboardSkeleton /> : null}
      {isError ? <ErrorState onRetry={refreshDashboard} /> : null}
      {!isLoading && !isError && hasNoData ? <EmptyState title="No growth signals yet" description="Your workspace is ready, but the API returned no growth signals to display." /> : null}

      {!isLoading && !isError && dashboardData ? (
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
                    {recommendations.map((recommendation) => (
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



          <Box component="section" aria-labelledby="knowledge-intelligence-heading">
            <SectionHeader eyebrow="Knowledge Intelligence" title="Explainable signal importance" description="Stored knowledge items scored by freshness, authority, relevance, momentum, and confidence." />
            <Grid container spacing={2.5} sx={{ mt: 1 }}>
              {knowledgeItems.slice(0, 6).map((item) => {
                const overallScore = item.overall_score ?? 0;
                const scoreRows = [
                  ['Freshness', item.component_scores.freshness],
                  ['Authority', item.component_scores.authority],
                  ['Relevance', item.component_scores.relevance],
                  ['Momentum', item.component_scores.momentum],
                  ['Confidence', item.component_scores.confidence],
                ] as const;
                return (
                  <Grid key={item.id} item xs={12} md={6} xl={4}>
                    <DashboardCard>
                      <Stack spacing={2}>
                        <Stack direction="row" justifyContent="space-between" alignItems="flex-start" gap={2}>
                          <Box>
                            <Typography id="knowledge-intelligence-heading" variant="overline" color="text.secondary" fontWeight={800}>
                              {item.category}
                            </Typography>
                            <Typography variant="h6" component="h3">
                              {item.title}
                            </Typography>
                          </Box>
                          <Tooltip title="Priority is derived from the overall Intelligence Score.">
                            <Chip label={item.priority ?? 'Unranked'} color={item.priority === 'Critical' ? 'error' : item.priority === 'High' ? 'warning' : 'default'} size="small" />
                          </Tooltip>
                        </Stack>
                        <Box>
                          <Stack direction="row" justifyContent="space-between" alignItems="center" sx={{ mb: 1 }}>
                            <Typography variant="body2" color="text.secondary" fontWeight={800}>
                              Overall Intelligence Score
                            </Typography>
                            <Typography variant="h6">{Math.round(overallScore)}</Typography>
                          </Stack>
                          <LinearProgress variant="determinate" value={overallScore} sx={{ height: 8, borderRadius: 99 }} />
                        </Box>
                        <Chip label={`Status: ${item.processing_status}`} variant="outlined" size="small" sx={{ alignSelf: 'flex-start' }} />
                        <Accordion disableGutters elevation={0} sx={{ bgcolor: 'transparent' }}>
                          <AccordionSummary expandIcon={<ExpandMoreIcon />}>
                            <Typography fontWeight={800}>Component Scores</Typography>
                          </AccordionSummary>
                          <AccordionDetails>
                            <Stack spacing={1.25}>
                              {scoreRows.map(([label, value]) => (
                                <Box key={label}>
                                  <Stack direction="row" justifyContent="space-between">
                                    <Typography variant="body2">{label}</Typography>
                                    <Typography variant="body2" fontWeight={800}>{value == null ? 'Pending' : Math.round(value)}</Typography>
                                  </Stack>
                                  <LinearProgress variant="determinate" value={value ?? 0} sx={{ height: 6, borderRadius: 99 }} />
                                </Box>
                              ))}
                            </Stack>
                          </AccordionDetails>
                        </Accordion>
                      </Stack>
                    </DashboardCard>
                  </Grid>
                );
              })}
            </Grid>
          </Box>

          <Box component="section" aria-labelledby="trend-radar-heading">
            <SectionHeader eyebrow="Trend Radar" title="Signals to turn into content" description="Mock source badges show where each trend would be validated when live integrations arrive." />
            <Stack spacing={3} sx={{ mt: 3 }}>
              {trendsByCategory.map(({ category, trends: categoryTrends }) => (
                <Box key={category}>
                  <Typography id={category === 'AI' ? 'trend-radar-heading' : undefined} variant="h6" component="h3" sx={{ mb: 2 }}>
                    {category}
                  </Typography>
                  <Grid container spacing={2.5}>
                    {categoryTrends.map((trend) => (
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
